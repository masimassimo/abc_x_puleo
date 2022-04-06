# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class saleOrder(models.Model):
    _inherit = "sale.order"
    _name = "sale.order"
    
    #Funzione che permette di calcolare le provvigioni su un determinato Ordine di vendita. Essa ogni volta che viene aggiunto o rimosso un prodotto dall'ordine di vendita viene chiamata e
    #a seconda degli agenti relativi al campo partner_id dell'ordine di vendita e alle loro regole di provvigione, se è il caso (una regola matcha con un prodotto in ordine) va a scrivere 
    #la provvigione per l'agente. 
    @api.depends("order_line")
    def _calcolaProvvigioni(self):
        
        for record in self:
            cliente_direzionale = False
            contatto_preferito = False
            agenti = ""
            addetto_vendite = self.env['res.config.settings'].get_values()['addetto_vendite']
            righe_ordine_vendita = record.order_line
            
            if(record.partner_id.direzionale):
                _logger.info("Il Cliente %s è un cliente Direzionale", record.partner_id.name)
                cliente_direzionale = True
                
            if(record.partner_id.direzionale):
                _logger.info("Il Cliente %s è un cliente Direzionale", record.partner_id.name)
                cliente_direzionale = True
              
            for riga_ordine_vendita in righe_ordine_vendita:
                provvigioni_sline_ids = []
                righe_da_eliminare = [] #Check
                righe_provvigioni_attuali = record.provvigioni_sline_ids
                
                for riga_provvigione_attuale in righe_provvigioni_attuali:
                    if ((riga_provvigione_attuale.riferimento_riga_ordine.id == riga_ordine_vendita.id and not riga_provvigione_attuale.riferimento_ordine_fittizio) or riga_provvigione_attuale.tipo == "regola_percentuale_fissa"):
                        righe_da_eliminare.append(riga_provvigione_attuale)
                    
                    if(righe_da_eliminare):
                        for riga_da_eliminare in righe_da_eliminare:
                            _logger.info("Adesso elimino la riga: %s", riga_da_eliminare.id)
                            riga_da_eliminare.unlink()
                            
                #Se il flag del menù di configurazione è attivo viene considerato come unico agente l'addetto vendite. Altrimenti tutti quelli presenti nel campo agenti_ids.
                if(addetto_vendite):
                    agenti = record.user_id
                    _logger.info("Il flag è attivo e l'agente è: %s", record.user_id)
                
                else:
                    if(record.partner_id.agenti_ids):
                        agenti = record.partner_id.agenti_ids
                if(agenti):
                    
                    for agente in agenti:
                        provvigioni_agente = agente.provvigioni_ids
                        
                        for provvigione_agente_check_preferito in provvigioni_agente:
                            regola_percentuale_fissa = False
                            if(provvigione_agente_check_preferito.contatto_preferito == record.partner_id):
                                contatto_preferito = True
                                _logger.info("La regola %s ha il contatto preferito", provvigione_agente_check_preferito.name)
                                
                                # Provvigione per contatto_preferito #
                                ######################################
                                
                                tipo = provvigione_agente_check_preferito.tipo
                                percentuale = provvigione_agente_check_preferito.percentuale
                                importo_percentuale = 0
                                contatto = provvigione_agente_check_preferito.contatto
                                prodotto = None
                                categoria_prodotto = None
                                prodotto_attuale = None #Check
                                categoria_prodotto_attuale = None #Check

                                if(percentuale != 0):
                                    importo = percentuale/100.0 * (riga_ordine_vendita.price_unit * riga_ordine_vendita.product_uom_qty)
                                    importo_percentuale = importo
                                else:
                                    importo = provvigione_agente_check_preferito.importo * riga_ordine_vendita.product_uom_qty
                                
                                if tipo == "regola_percentuale_fissa":
                                    importo = percentuale/100.0 * record.amount_total
                                    regola_percentuale_fissa = True

                                if tipo == "regola_prodotto":
                                    prodotto = provvigione_agente_check_preferito.prodotto.id

                                if tipo == "regola_categoria_prodotto":
                                    categoria_prodotto = provvigione_agente_check_preferito.categoria_prodotto.id

                                if riga_ordine_vendita.product_id:
                                    prodotto_attuale = riga_ordine_vendita.product_id.id

                                if riga_ordine_vendita.product_id.categ_id:
                                    categoria_prodotto_attuale = riga_ordine_vendita.product_id.categ_id.id

                                if ((prodotto_attuale != None and categoria_prodotto == categoria_prodotto_attuale) or regola_percentuale_fissa):
                                    _logger.info("-------- Aggiunta provvigione CONTATTO_PREFERITO per CATEGORIA. ------- ")
                                    provvigioni_sline_ids.append((0, 0, {
                                                                        "tipo": tipo,
                                                                        "categoria_prodotto": categoria_prodotto,
                                                                        "importo": importo,
                                                                        "importo_percentuale": importo_percentuale,
                                                                        "percentuale": percentuale,
                                                                        "contatto": contatto.id,
                                                                        "riferimento_riga_ordine": riga_ordine_vendita.id,
                                                
                                                                        }))
                                elif ((prodotto_attuale != None and prodotto == prodotto_attuale) or regola_percentuale_fissa):
                                    _logger.info("-------- Aggiunta provvigione CONTATTO_PREFERITO per PRODOTTO. ------- ")
                                    provvigioni_sline_ids.append((0, 0, {
                                                                        "tipo": tipo,
                                                                        "prodotto": prodotto,
                                                                        "importo": importo,
                                                                        "importo_percentuale": importo_percentuale,
                                                                        "percentuale": percentuale,
                                                                        "contatto": contatto.id,
                                                                        "riferimento_riga_ordine": riga_ordine_vendita.id,
                                                                        }))
 
                                
                                ######################################
                                
                                
                        if(not contatto_preferito):
                            for provvigione_agente in provvigioni_agente:
                                regola_percentuale_fissa = False
                                
                                # Provvigione per cliente_direzionale #
                                #######################################

                                if(cliente_direzionale and provvigione_agente.direzionale and not provvigione_agente.contatto_preferito):
                                    tipo = provvigione_agente.tipo
                                    percentuale = provvigione_agente.percentuale
                                    importo_percentuale = 0
                                    contatto = provvigione_agente.contatto
                                    prodotto = None
                                    categoria_prodotto = None
                                    prodotto_attuale = None #Check
                                    categoria_prodotto_attuale = None #Check

                                    if(percentuale != 0):
                                        importo = percentuale/100.0 * (riga_ordine_vendita.price_unit * riga_ordine_vendita.product_uom_qty)
                                        importo_percentuale = importo
                                    else:
                                        importo = provvigione_agente.importo * riga_ordine_vendita.product_uom_qty
                                        
                                    if tipo == "regola_percentuale_fissa":
                                        importo = percentuale/100.0 * record.amount_total
                                        regola_percentuale_fissa = True
                                        
                                    if tipo == "regola_prodotto":
                                        prodotto = provvigione_agente.prodotto.id

                                    if tipo == "regola_categoria_prodotto":
                                        categoria_prodotto = provvigione_agente.categoria_prodotto.id

                                    if riga_ordine_vendita.product_id:
                                        prodotto_attuale = riga_ordine_vendita.product_id.id

                                    if riga_ordine_vendita.product_id.categ_id:
                                        categoria_prodotto_attuale = riga_ordine_vendita.product_id.categ_id.id

                                    if ((prodotto_attuale != None and categoria_prodotto == categoria_prodotto_attuale) or regola_percentuale_fissa):
                                        _logger.info("-------- Aggiunta provvigione DIREZIONALE per CATEGORIA. ------- ")
                                        provvigioni_sline_ids.append((0, 0, {
                                                                            "tipo": tipo,
                                                                            "categoria_prodotto": categoria_prodotto,
                                                                            "importo": importo,
                                                                            "importo_percentuale": importo_percentuale,
                                                                            "percentuale": percentuale,
                                                                            "contatto": contatto.id,
                                                                            "riferimento_riga_ordine": riga_ordine_vendita.id,
                                                                            }))
                                    elif ((prodotto_attuale != None and prodotto == prodotto_attuale) or regola_percentuale_fissa):
                                        _logger.info("-------- Aggiunta provvigione DIREZIONALE per PRODOTTO. ------- ")
                                        provvigioni_sline_ids.append((0, 0, {
                                                                            "tipo": tipo,
                                                                            "prodotto": prodotto,
                                                                            "importo": importo,
                                                                            "importo_percentuale": importo_percentuale,
                                                                            "percentuale": percentuale,
                                                                            "contatto": contatto.id,
                                                                            "riferimento_riga_ordine": riga_ordine_vendita.id,
                                                                            }))
                                # Provvigione per standard #
                                ############################

                                if(not cliente_direzionale and not provvigione_agente.direzionale and not provvigione_agente.contatto_preferito):
                                    tipo = provvigione_agente.tipo
                                    percentuale = provvigione_agente.percentuale
                                    importo_percentuale = 0
                                    contatto = provvigione_agente.contatto
                                    prodotto = None
                                    categoria_prodotto = None
                                    prodotto_attuale = None #Check
                                    categoria_prodotto_attuale = None #Check

                                    if(percentuale != 0):
                                        importo = percentuale/100.0 * (riga_ordine_vendita.price_unit * riga_ordine_vendita.product_uom_qty)
                                        importo_percentuale = importo
                                    else:
                                        importo = provvigione_agente.importo * riga_ordine_vendita.product_uom_qty
                                        
                                    if tipo == "regola_percentuale_fissa":
                                        importo = percentuale/100.0 * record.amount_total
                                        regola_percentuale_fissa = True
                                        _logger.info("regola_percentuale_fissa : %s", regola_percentuale_fissa)

                                    if tipo == "regola_prodotto":
                                        prodotto = provvigione_agente.prodotto.id

                                    if tipo == "regola_categoria_prodotto":
                                        categoria_prodotto = provvigione_agente.categoria_prodotto.id

                                    if riga_ordine_vendita.product_id:
                                        prodotto_attuale = riga_ordine_vendita.product_id.id

                                    if riga_ordine_vendita.product_id.categ_id:
                                        categoria_prodotto_attuale = riga_ordine_vendita.product_id.categ_id.id
                                        
                                    _logger.info("CONDIZIONE : %s", ((prodotto_attuale != None and categoria_prodotto == categoria_prodotto_attuale) or regola_percentuale_fissa))

                                    if ((prodotto_attuale != None and categoria_prodotto == categoria_prodotto_attuale) or regola_percentuale_fissa):
                                        _logger.info("-------- Aggiunta provvigione NON DIREZIONALE per CATEGORIA. ------- ")
                                        provvigioni_sline_ids.append((0, 0, {
                                                                            "tipo": tipo,
                                                                            "categoria_prodotto": categoria_prodotto,
                                                                            "importo": importo,
                                                                            "importo_percentuale": importo_percentuale,
                                                                            "percentuale": percentuale,
                                                                            "contatto": contatto.id,
                                                                            "riferimento_riga_ordine": riga_ordine_vendita.id,

                                                                            }))
                                    elif ((prodotto_attuale != None and prodotto == prodotto_attuale) or regola_percentuale_fissa):
                                        _logger.info("-------- Aggiunta provvigione NON DIREZIONALE per PRODOTTO. ------- ")
                                        provvigioni_sline_ids.append((0, 0, {
                                                                            "tipo": tipo,
                                                                            "prodotto": prodotto,
                                                                            "importo": importo,
                                                                            "importo_percentuale": importo_percentuale,
                                                                            "percentuale": percentuale,
                                                                            "contatto": contatto.id,
                                                                            "riferimento_riga_ordine": riga_ordine_vendita.id,
                                                                            }))

                if(provvigioni_sline_ids):     
                    _logger.info("Provvigione line_ids : %s", provvigioni_sline_ids)
            
                    record.write({"provvigioni_sline_ids": provvigioni_sline_ids})
            
                    _logger.info("-------- Ho terminato di scrivere le provvigioni! ------- ")
                else:
                    _logger.info("Non ho scritto nessuna provvigione per il prodotto: %s", riga_ordine_vendita.product_id.name)
             
    #Campo dummy che mi permette di calcolare le provvigioni relative ad un ordine di vendita.        
    aggiungi_provvigioni = fields.Boolean(string = "Aggiungi provvigioni", help = "Campo dummy che mi permette di calcolare le provvigioni relative ad un ordine di vendita.", store = True, compute = _calcolaProvvigioni)
        
    #Funzione che calcola il totale degli importi di provvigione.
    @api.depends("provvigioni_sline_ids.importo")
    def calcola_totale_provvigioni_s(self):
        for record in self:
            totale_provvigioni_s = 0
            righe_provvigioni = record.provvigioni_sline_ids
            for riga_provvigione in righe_provvigioni:
                totale_provvigioni_s += riga_provvigione.importo
            record.update({"totale_provvigioni_s": totale_provvigioni_s})
            _logger.info(" -------- calcola_totale_provvigioni_s -------- ")
    
    provvigioni_sline_ids = fields.One2many(comodel_name = "abc.lines_sales_commission", inverse_name="riferimento_ordine", string = "Righe provvigioni", help = "Specchietto righe provvigioni.", tracking = True, readonly = True, states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},)
        
    @api.onchange("provvigioni_sline_ids")
    def calcola_nuovo_importo(self):
        _logger.info("calcola_nuovo_importo")
        for record in self:
            righe_provvigioni = record.provvigioni_sline_ids
            for riga_provvigione in righe_provvigioni:
                if riga_provvigione.percentuale != 0:
                    nuovo_importo = riga_provvigione.percentuale/100.0 * (riga_provvigione.riferimento_riga_ordine.price_unit * riga_provvigione.riferimento_riga_ordine.product_uom_qty)
                    _logger.info("nuovo_importo %s", nuovo_importo)
                    riga_provvigione.update({'importo': nuovo_importo})
    
    #Campo totale_provvigioni che somma gli importi di tutte le singole righe di provvigione.
    totale_provvigioni_s = fields.Monetary(string = "Totale provvigioni", readonly = True, tracking = True, help = "La somma degli importi delle singole righe di provvigione.", compute = "calcola_totale_provvigioni_s")