# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Dichiarazione iniziale del modulo ABC - abc_fattura_imm_e_diff_puleo.
class abc_fattura_imm_e_diff_puleo(models.Model):
    _name = 'abc_fattura_imm_e_diff_puleo.abc_fattura_imm_e_diff_puleo'
    _description = 'abc_fattura_imm_e_diff_puleo.abc_fattura_imm_e_diff_puleo'
    
#Eredito il modulo account.move per accedervi.
class accountMove(models.Model):
    _name = "account.move"
    _inherit = "account.move"
    
    #agente = fields.Many2one('res.partner', string= "Addetto vendite", related="invoice_line_ids.sale_line_ids.order_id.user_id", store = True, readonly = False)
    
#Eredito il modulo sale.order per accedervi.
class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = "sale.order"
