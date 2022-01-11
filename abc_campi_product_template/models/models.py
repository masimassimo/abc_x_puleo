# -*- coding: utf-8 -*-

from odoo import models, fields, api


class abc_campi_product_template(models.Model):
    _name = 'abc_campi_product_template.abc_campi_product_template'
    _description = 'abc_campi_product_template.abc_campi_product_template'

class productTemplate(models.Model):
    _name= "product.template"
    _inherit = "product.template"
    #TEST
    
    codice_prodotto_sam = fields.Char(string = "Codice prodotto SAM", store = True)
    
    tipo_articolo = fields.Selection([("componente", "Componente"), ("insieme", "Insieme"), ("servizio", "Servizio"), ("sottoinsieme", "Sottoinsieme")], string = "Tipo Articolo", store = True)
    
    codice_merce = fields.Char(string = "Codice Merce", store = True)
    descrizione_nomenclatura_combinata = fields.Char(string = "Descrizione nomenclatura combinata", store = True)
    
    tipo_produzione_articolo = fields.Selection([("commerciale", "Commerciale"), ("fantasma", "Fantasma"), ("interno", "Interno"),], string = "Tipo produzione articolo", store = True)
    
    stato_articolo = fields.Selection([("gestito", "Gestito"), ("installabile", "Installabile"), ("superato", "Superato"),], string = "Stato articolo", store = True)
    
    
    

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
