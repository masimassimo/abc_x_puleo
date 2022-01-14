# -*- coding: utf-8 -*-

from odoo import models, fields, api


class abc_campi_4_0(models.Model):
    _name = 'abc_campi_4_0.abc_campi_4_0'
    _description = 'abc_campi_4_0.abc_campi_4_0'

class mrpProduction(models.Model):
    _name= "mrp.production"
    _inherit = "mrp.production"
    
    qty_scarto_1 = fields.Float(string="Quantità Scartate 1", store=True)
    qty_scarto_2 = fields.Float(string="Quantità Scartate 2", store=True)

    '''def _set_qty_scarto_1(self, qty):
        qty_scarto_1 = (qty)
    def _set_qty_scarto_2(self, qty):
        qty_scarto_2 = (qty)'''
            
            

class MrpWorkorder(models.Model):
    _name = 'mrp.workorder'
    _inherit = 'mrp.workorder'
    
    qty_scarto_1 = fields.Float(
        compute='_compute_qty_scarto_1', inverse='_set_qty_scarto_1',
        string='Currently Discarded Quantity 1', digits='Product Unit of Measure')

    
    @api.depends('production_id.qty_scarto_1')
    def _compute_qty_scarto_1(self):
        for workorder in self:
            workorder.qty_scarto_1 = workorder.production_id.qty_scarto_1
           

    def _set_qty_scarto_1(self):
        for workorder in self:
            if workorder.qty_scarto_1 != 0 and workorder.production_id.qty_scarto_1 != workorder.qty_scarto_1:
                workorder.production_id.qty_scarto_1 = workorder.qty_scarto_1
                #workorder.production_id._set_qty_scarto_1(qty_scarto_1)
                
    qty_scarto_2 = fields.Float(
        compute='_compute_qty_scarto_2', inverse='_set_qty_scarto_2',
        string='Currently Discarded Quantity 2', digits='Product Unit of Measure')

    
    @api.depends('production_id.qty_scarto_2')
    def _compute_qty_scarto_2(self):
        for workorder in self:
            workorder.qty_scarto_2 = workorder.production_id.qty_scarto_2
           

    def _set_qty_scarto_2(self):
        for workorder in self:
            if workorder.qty_scarto_2 != 0 and workorder.production_id.qty_scarto_2 != workorder.qty_scarto_2:
                workorder.production_id.qty_scarto_2 = workorder.qty_scarto_2
                #workorder.production_id._set_qty_scarto_2(qty_scarto_2)
