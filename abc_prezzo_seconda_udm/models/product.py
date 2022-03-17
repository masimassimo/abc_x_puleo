# -*- coding: utf-8 -*-
from odoo import models, fields, api

class productSecondaryUnit(models.Model):
    _inherit = "product.secondary.unit"
    _name = "product.secondary.unit"
    
    fattore_inverso = fields.Float(string = "Fattore di conversione", help = "Fattore da compilare affinchè si cambi quello principale.", tracking = True, digits = (12,4), default = 0.0000, required = True)
    
    factor = fields.Float(string="Secondary Unit Factor", default=0.0000, digits= (12,4), required=True)
    
    costo_secondario = fields.Float("Costo secondario", tracking = True)
    
    @api.onchange("fattore_inverso")
    def ricalcola_factor(self):
            for record in self:
                if(record.fattore_inverso != 0.0000):
                    record.update({'factor': 1/record.fattore_inverso})
            
            
    def name_get(self):
        result = []
        for unit in self:
            result.append((unit.id, "{unit_name}-{factor}".format(unit_name=unit.uom_id.name, factor=round(unit.fattore_inverso, 4),)))
        return result
    
