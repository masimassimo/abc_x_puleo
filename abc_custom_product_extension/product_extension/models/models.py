# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductExtension(models.Model):
       _name = 'product_extension.product_extension'
       _description = 'Product Extension'

#Eredito il modulo ProductTemplate per accedere alla vista.    
class ProductTemplate(models.Model):
     _inherit = 'product.template'

#Eredito il modulo SaleOrder per accedere alla vista.
class SaleOrder(models.Model):
     _inherit = 'sale.order'