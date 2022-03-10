# -*- coding: utf-8 -*-

from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    cmr_code = fields.Integer(
        string='CMR Code',
        default=0,
        help="Code needed for CMR Report",
    )
    
    vettore_cmr = fields.Many2one("res.partner", string = "Vettore CMR", help = "Vettore CMR", tracking = True)
    targa_motrice_cmr = fields.Char(string = "Targa motrice", help = "La targa del mezzo.", tracking = True)
    targa_rimorchio_cmr = fields.Char(string = "Targa rimorchio", help = "La targa del rimorchio.", tracking = True)
    
    totale_peso_lordo_cmr = fields.Char(string = "Peso lordo totale", help = "Il peso lordo complessivo di tutti gli articoli.", tracking = True)
    totale_volume_cmr = fields.Char(string = "Volume totale", help = "Il volume complessivo di tutti gli articoli.", tracking = True)
    