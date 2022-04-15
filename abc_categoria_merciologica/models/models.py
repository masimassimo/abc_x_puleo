# -*- coding: utf-8 -*-

from odoo import models, fields, api


class abc_categoria_merciologica(models.Model):
    _name = 'abc_categoria_merciologica.abc_categoria_merciologica'
    _description = 'abc_categoria_merciologica.abc_categoria_merciologica'

class productCategory(models.Model):
    _name = "product.category"
    _inherit = "product.category"
    
    categoria_merciologica = fields.Char(string = "Categoria merceologica", store = True)
