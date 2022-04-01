# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class accountMove(models.Model):
    _inherit = "account.move"
    _name = "account.move"
    
    #Funzione che calcola il totale degli importi di provvigione.
    @api.depends("provvigioni_aline_ids.importo")
    def calcola_totale_provvigioni_a(self):
        for record in self:
            totale_provvigioni_a = 0
            righe_provvigioni = record.provvigioni_aline_ids
            for riga_provvigione in righe_provvigioni:
                totale_provvigioni_a += riga_provvigione.importo
                riga_provvigione.write({"riferimento_fattura": record.id})
            record.update({"totale_provvigioni_a": totale_provvigioni_a})
            
            
    @api.depends("invoice_line_ids", "invoice_line_ids.sale_line_ids.order_id.provvigioni_sline_ids")
    def _aggiungi_provvigioni_rimanenti(self):
        
        for record in self:
            provvigioni_aline_ids = []
            righe_fattura = record.invoice_line_ids

            for riga_fattura in righe_fattura:
                
                if(riga_fattura.sale_line_ids):
                    righe_ordine_vendita = riga_fattura.sale_line_ids

                    for riga_ordine_vendita in righe_ordine_vendita:
                        ordine_vendita = riga_ordine_vendita.order_id

                        if(ordine_vendita.provvigioni_sline_ids):
                            righe_provvigione = ordine_vendita.provvigioni_sline_ids
                            
                            for riga_provvigione in righe_provvigione:
                                riga_provvigione.update({"riferimento_fattura": record.id})

                    
            _logger.info(" ------ Provvigioni aggiornate con il Riferimento Fattura. ------")
        
    
    provvigioni_rimanenti = fields.Boolean(string = "Provvigioni rimanenti", compute = _aggiungi_provvigioni_rimanenti, store = True)
    
    @api.depends("payment_state")
    def _matura_provvigioni(self):
        for record in self:
            _logger.info("Dentro _matura_provvigioni")
            if(record.provvigioni_aline_ids and record.payment_state == "in_payment"): #DA MODIFICARE CON PAID
                righe_provvigioni_fattura = record.provvigioni_aline_ids
                
                for riga_provvigioni_fattura in righe_provvigioni_fattura:
                    riga_provvigioni_fattura.update({"maturata": True})
                
            
    
    #Campo che esegue la funzione _matura_provvigioni non appena una fattura viene pagata.
    matura_provvigioni = fields.Boolean(string = "Matura provvigioni", compute = _matura_provvigioni, store = True)
    
    provvigioni_aline_ids = fields.One2many(comodel_name = "abc.lines_sales_commission", inverse_name="riferimento_fattura", string = "Righe provvigioni", help = "Specchietto righe provvigioni.", tracking = True, readonly = False)
    
    #Campo totale_provvigioni che somma gli importi di tutte le singole righe di provvigione.
    totale_provvigioni_a = fields.Monetary(string = "Totale provvigioni", readonly = True, tracking = True, help = "La somma degli importi delle singole righe di provvigione.", compute = "calcola_totale_provvigioni_a")