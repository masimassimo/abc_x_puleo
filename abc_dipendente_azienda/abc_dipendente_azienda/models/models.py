# -*- coding: utf-8 -*-
from odoo import models, fields, api


class abc_dipendente_azienda(models.Model):
     _name = 'abc_dipendente_azienda.abc_dipendente_azienda'
     _description = 'abc_dipendente_azienda.abc_dipendente_azienda'
    
    
#Eredito il modulo "SaleOrder" per accedere alla vista.
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    nominativo_di_riferimento = fields.Many2one(
        'res.partner', string='Nominativo di riferimento', readonly=False,
        #states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
        change_default=True, index=True, tracking=1,
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id), ('parent_id', '=', partner_id)]",)
    
class StockDeliveryNote(models.Model):
    _name = "stock.delivery.note"
    _inherit = "stock.delivery.note"
    
    nominativo_di_riferimento = fields.Many2one(string = 'Nominativo di riferimento', related = "sale_ids.nominativo_di_riferimento", readonly=False, store=True, copy=True)
