# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class saleOrder(models.Model):
    _inherit = "sale.order"
    _name = "sale.order"
    
    #Funzione che calcola il totale degli importi di provvigione.
    @api.depends("provvigioni_sline_ids.importo")
    def calcola_totale_provvigioni_s(self):
        for record in self:
            totale_provvigioni_s = 0
            righe_provvigioni = record.provvigioni_sline_ids
            for riga_provvigione in righe_provvigioni:
                totale_provvigioni_s += riga_provvigione.importo
            record.update({"totale_provvigioni_s": totale_provvigioni_s})
    
    provvigioni_sline_ids = fields.One2many(comodel_name = "abc.lines_sales_commission", inverse_name="riferimento_ordine", string = "Righe provvigioni", help = "Specchietto righe provvigioni.", tracking = True)
    
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
                    
class saleOrderLine(models.Model):
    _inherit = "sale.order.line"
    _name = "sale.order.line"
    
    def write(self, vals):
        result = super(saleOrderLine, self).write(vals)
        
        for record in self:
            righe_da_eliminare = []
            n_provvigioni = 0
            righe_provvigioni_attuali = record.order_id.provvigioni_sline_ids
            if record.order_id.partner_id.agenti_ids:
                agenti = record.order_id.partner_id.agenti_ids
                
                for agente in agenti:
                    provvigioni_agente = agente.provvigioni_ids
                    
                    for provvigione_agente in provvigioni_agente:
                                        tipo = provvigione_agente.tipo
                                        percentuale = provvigione_agente.percentuale
                                        importo_percentuale = 0
                                        
                                        if(percentuale != 0):
                                            importo = percentuale/100.0 * (record.price_unit * record.product_uom_qty)
                                            importo_percentuale = importo
                                        else:
                                            importo = provvigione_agente.importo * record.product_uom_qty
                                        
                                        contatto = provvigione_agente.contatto
                                        prodotto = None
                                        categoria_prodotto = None
                                        prodotto_attuale = None
                                        categoria_prodotto_attuale = None

                                        if tipo == "regola_prodotto":
                                            prodotto = provvigione_agente.prodotto

                                        if tipo == "regola_categoria_prodotto":
                                            categoria_prodotto = provvigione_agente.categoria_prodotto

                                        if record.product_id:
                                            prodotto_attuale = record.product_id

                                        if record.product_id.categ_id:
                                            categoria_prodotto_attuale = record.product_id.categ_id

                                     
                                        if (prodotto_attuale != None and categoria_prodotto == categoria_prodotto_attuale ):
                                                    n_provvigioni += 1
                                                    _logger.info("N Provv: %s", n_provvigioni)
                                                    _logger.info("-------- IF VERO ------- ")
                                                    record.order_id.provvigioni_sline_ids = [(0, 0, {
                                                                                            "tipo": tipo,
                                                                                            "categoria_prodotto": categoria_prodotto.id,
                                                                                            "importo": importo,
                                                                                            "importo_percentuale": importo_percentuale,
                                                                                            "percentuale": percentuale,
                                                                                            "contatto": contatto.id,
                                                                                            "riferimento_riga_ordine": record.id
                                                                                            })]
                                        elif (prodotto_attuale != None and prodotto == prodotto_attuale):
                                                    n_provvigioni += 1
                                                    _logger.info("N Provv: %s", n_provvigioni)
                                                    _logger.info("-------- IF VERO ------- ")
                                                    record.order_id.provvigioni_sline_ids = [(0, 0, {
                                                                                            "tipo": tipo,
                                                                                            "prodotto": prodotto.id,
                                                                                            "importo": importo,
                                                                                            "importo_percentuale": importo_percentuale,
                                                                                            "percentuale": percentuale,
                                                                                            "contatto": contatto.id,
                                                                                            "riferimento_riga_ordine": record.id
                                                                                            })]
                #Snippet che permette di eliminare i doppioni non aggiornati!
                if len(record.order_id.provvigioni_sline_ids) > n_provvigioni:
                        _logger.info("IF PROVV: %s", n_provvigioni)
                        _logger.info("LOG ---------- righe_provvigioni_attuali %s", righe_provvigioni_attuali)
                        
                        for riga_provvigione_attuale in righe_provvigioni_attuali:
                            if riga_provvigione_attuale.riferimento_riga_ordine.id == record.id:
                                _logger.info("RIGHE PROVVIGIONI UGUALI")
                                righe_da_eliminare.append(riga_provvigione_attuale)
                                
                        if(righe_da_eliminare):
                            for riga_da_eliminare in righe_da_eliminare:
                                riga_da_eliminare.unlink()
                                _logger.info("Riga %s eliminata!", riga_da_eliminare.id)
                    
        return result