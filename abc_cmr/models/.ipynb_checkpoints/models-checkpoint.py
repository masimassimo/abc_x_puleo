# -*- coding: utf-8 -*-

from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    cmr_code = fields.Integer(
        string='CMR Code',
        default=0,
        help="Code needed for CMR Report",
    )