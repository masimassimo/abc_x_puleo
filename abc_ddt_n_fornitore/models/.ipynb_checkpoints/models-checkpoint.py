# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class StockDeliveryNote(models.Model):
    _name = "stock.delivery.note"
    _inherit = "stock.delivery.note"
    
    n_ddt_fornitore = fields.Char(string="N° DDT Fornitore")

class StockPicking(models.Model):
    _name = "stock.picking"
    _inherit = "stock.picking"
    
    n_ddt_fornitore = fields.Char(string="N° DDT Fornitore", related='delivery_note_id.n_ddt_fornitore', readonly=False)
    
class purchaseOrder(models.Model):
    _name = "purchase.order"
    _inherit = "purchase.order"
    
    
    #Funzione che mi permette di concatenare all'interno del campo ddt_con_data il numero ddt fornitore e la relativa data.
    @api.depends("delivery_note_ids")
    def compute_ddt_con_data(self):
        for record in self:
            record.ddt_con_data = ""
            if(record.delivery_note_ids):
                ddts = record.delivery_note_ids
                for ddt in ddts:
                    if(ddt.n_ddt_fornitore):
                        record.ddt_con_data = record.ddt_con_data + " " + str(ddt.n_ddt_fornitore) + " - " + ddt.date.strftime("%d/%m/%Y") + "; "
                    else:
                        record.ddt_con_data = ""
    
    #Campo many2many che permette di visualizzare i DDT correlati all'ordine di acquisto con la data del DDT.
    ddt_con_data = fields.Char(string = "DdT con data", help = "DDT correlati all'ordine di acquisto con la data del DDT.", store = False, compute = compute_ddt_con_data, default = "", readonly = False)