# -*- coding: utf-8 -*-

from odoo import models, fields, api


class abc_no_edit_products(models.Model):
     _name = 'abc_no_edit_products.abc_no_edit_products'
     _description = 'abc_no_edit_products.abc_no_edit_products'
    
class saleOrder(models.Model):
    _inherit = "sale.order"
    _name = "sale.order"

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
