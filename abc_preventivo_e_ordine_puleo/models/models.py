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
    
    flag_prezzo_configurazione_variante = fields.Boolean(string = "Prezzo configurazione variante", default = False, tracking = True, help = "Flag che attiva la possibilità di vedere i prezzi delle singole configurazioni delle varianti all'interno della descrizione del prodotto.")
    
    @api.onchange("flag_prezzo_configurazione_variante")
    def funzione(self):
        for record in self:
            if(record.flag_prezzo_configurazione_variante):
                if(record.order_line):
                    righe_ordine = record.order_line
                    _logger.info("Righe ordine %s", righe_ordine)
                    for riga_ordine in righe_ordine:
                        descrizione_prodotto_attuale = riga_ordine.name
                        _logger.info("Descrizione %s", descrizione_prodotto_attuale)
                        riga_ordine.update({'name': "CIAOOOOOOOOO"})
                else:
                    raise ValidationError("Inserire almeno un prodotto.")
                
            
