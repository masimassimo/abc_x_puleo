# -*- coding: utf-8 -*-

from odoo import models, fields, api


class abc_campi_4_0(models.Model):
    _name = 'abc_campi_4_0.abc_campi_4_0'
    _description = 'abc_campi_4_0.abc_campi_4_0'

class mrpProduction(models.Model):
    _name= "mrp.production"
    _inherit = "mrp.production"
    
    scarto_1 = fields.Float(string="Scartate 1", store=True)
    qty_scarto_1 = fields.Float(string="Quantità Scartate 1", store=True)
    scarto_2 = fields.Float(string="Scartate 2", store=True)
    qty_scarto_2 = fields.Float(string="Quantità Scartate 2", store=True)
