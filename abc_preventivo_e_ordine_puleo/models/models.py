# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)

class abc_preventivo_e_ordinevendita_puleo(models.Model):
    _name = 'abc_preventivo_e_ordine_puleo.abc_preventivo_e_ordine_puleo'
    _description = 'abc_preventivo_e_ordine_puleo.abc_preventivo_e_ordine_puleo'


#Eredito il modulo sale.order così vi posso accedere.    
class saleOrder(models.Model):
    _name = "sale.order"
    _inherit = "sale.order"
    
    #Campo booleano che permette di triggerare la funzione 'funzione'.
    flag_prezzo_configurazione_variante = fields.Boolean(string = "Prezzo configurazione variante", default = False, tracking = True, help = "Flag che attiva la possibilità di vedere i prezzi delle singole configurazioni delle varianti all'interno della descrizione del prodotto.")
    
    #Funzione che permette di cambiare la descrizione del prodotto qualora si selezionasse il flag 'flag_prezzo_configurazione_variante'. Nella descrizione
    #compariranno i prezzi delle singole configurazioni varianti. 
    @api.onchange("flag_prezzo_configurazione_variante")
    def funzione(self):
        for record in self:
            simbolo_euro = (u"\N{euro sign}")                
            righe_ordine = record.order_line
            
            if(record.flag_prezzo_configurazione_variante):
                _logger.info("Righe ordine %s", righe_ordine)
                for riga_ordine in righe_ordine:
                    if(riga_ordine.product_id.product_template_attribute_value_ids):
                        attributi = ""
                        descrizione_prodotto_attuale = riga_ordine.name
                        nome_prodotto = riga_ordine.product_id.name
                        attributi_prodotto = riga_ordine.product_id.product_template_attribute_value_ids
                        
                        for attributo_prodotto in attributi_prodotto:
                            stringa_attributo = "- " + attributo_prodotto.name + " " + simbolo_euro + str(attributo_prodotto.price_extra)
                            
                            if(stringa_attributo not in descrizione_prodotto_attuale):
                                attributi = attributi + stringa_attributo + ", \n "
                                riga_ordine.update({'name': nome_prodotto + ": \n " + attributi + " "})

                        
            elif(not record.flag_prezzo_configurazione_variante):
                for riga_ordine in righe_ordine:
                    nome_prodotto = riga_ordine.product_id.display_name
                    if(not riga_ordine.product_id.product_template_attribute_value_ids):
                        descrizione_prodotto_attuale = riga_ordine.name
                        riga_ordine.update({'name': descrizione_prodotto_attuale})
                    else:
                        descrizione_prodotto_originaria = riga_ordine.product_template_id.description_sale
                        riga_ordine.update({'name': nome_prodotto + descrizione_prodotto_originaria})

                        
    @api.depends("partner_shipping_id")
    def _calcolaIndirizzoConsegna(self):
        for record in self:
            _logger.info("Dentro _calcolaIndirizzoConsegna")
            indirizzo_di_consegna = record.partner_shipping_id.name
            record.write({"calcola_indirizzo_consegna": indirizzo_di_consegna})
            
            

          
    #Campo che mi permette di calcolare l'indirizzo di consegna.
    calcola_indirizzo_consegna = fields.Char(string = "Calcola indirizzo consegna", store = False, compute = _calcolaIndirizzoConsegna)
