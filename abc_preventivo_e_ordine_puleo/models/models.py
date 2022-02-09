# -*- coding: utf-8 -*-

from odoo import models, fields, api


class abc_preventivo_e_ordinevendita_puleo(models.Model):
    _name = 'abc_preventivo_e_ordine_puleo.abc_preventivo_e_ordine_puleo'
    _description = 'abc_preventivo_e_ordine_puleo.abc_preventivo_e_ordine_puleo'


#Eredito il modulo sale.order così vi posso accedere.    
class saleOrder(models.Model):
    _name = "sale.order"
    _inherit = "sale.order"