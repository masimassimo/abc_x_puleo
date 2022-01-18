# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class abc_custom_header_puleo(models.Model):
#     _name = 'abc_custom_header_puleo.abc_custom_header_puleo'
#     _description = 'abc_custom_header_puleo.abc_custom_header_puleo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
