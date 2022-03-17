# -*- coding: utf-8 -*-
from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class PurchaseOrderLine(models.Model):
    _name = 'purchase.order.line'
    _inherit = 'purchase.order.line'
    
    price_unit_sec = fields.Float(string='Secondary Unit Price', digits='Product Price')
    
    @api.onchange("secondary_uom_id")
    def costo_secondario_default(self):
        for record in self:
            if(record.product_template_id.secondary_uom_ids):
                unita_secondarie = record.product_template_id.secondary_uom_ids
                for unita_secondaria in unita_secondarie:
                    if(record.secondary_uom_id == unita_secondaria):
                        _logger.info("UNITA ATTUALE %s, UNITA PRODOTTO %s", record.secondary_uom_id, unita_secondaria)
                        _logger.info(" ------ DENTRO IF ------ ")
                        record.update({'price_unit_sec': unita_secondaria.costo_secondario})
    
    
    @api.onchange('price_unit','product_uom','product_qty')
    def _ricalcolo_quantita_prezzo_sec(self):
        for order in self:
            if order.secondary_uom_qty != 0:
                order.price_unit_sec=(order.product_qty * order.price_unit) / order.secondary_uom_qty
        
    @api.onchange('price_unit_sec','secondary_uom_id','secondary_uom_qty')
    def _ricalcolo_quantita_prezzo(self):
        for order in self:
            if order.product_qty != 0:
                order.price_unit=(order.secondary_uom_qty * order.price_unit_sec) / order.product_qty
