# -*- coding: utf-8 -*-

from odoo import models, fields, api


class abc_ddt_puleo(models.Model):
     _name = 'abc_ddt_puleo.abc_ddt_puleo'
     _description = 'abc_ddt_puleo.abc_ddt_puleo'

    
    
class StockDeliveryNote(models.Model):
    _name = "stock.delivery.note"
    _inherit = "stock.delivery.note"
    
    def action_print(self):
        return self.env.ref(
            "abc_ddt_puleo.ddt_print_report_puleo"
        ).report_action(self)

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
