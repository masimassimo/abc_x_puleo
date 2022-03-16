# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class accountMove(models.Model):
    _inherit = "account.move"
    _name = "account.move"
    
    provvigioni_aline_ids = fields.One2many(comodel_name = "abc.lines_sales_commission", inverse_name="riferimento_fattura", string = "Righe provvigioni", help = "Specchietto righe provvigioni.", tracking = True, related = "invoice_line_ids.sale_line_ids.order_id.provvigioni_sline_ids", readonly = False)