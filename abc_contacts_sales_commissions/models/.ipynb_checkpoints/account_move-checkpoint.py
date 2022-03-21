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
    
    provvigioni_aline_ids = fields.One2many(comodel_name = "abc.lines_sales_commission", inverse_name="riferimento_fattura", string = "Righe provvigioni", help = "Specchietto righe provvigioni.", tracking = True, related = "invoice_line_ids.sale_line_ids.order_id.provvigioni_sline_ids", readonly = False)
    
    #Campo totale_provvigioni che somma gli importi di tutte le singole righe di provvigione.
    totale_provvigioni_a = fields.Monetary(string = "Totale provvigioni", readonly = True, tracking = True, help = "La somma degli importi delle singole righe di provvigione.", compute = "calcola_totale_provvigioni_a")