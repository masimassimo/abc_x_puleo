# -*- coding: utf-8 -*-

from odoo import models, fields, api


class abc_campi_product_template(models.Model):
    _name = 'abc_campi_product_template.abc_campi_product_template'
    _description = 'abc_campi_product_template.abc_campi_product_template'

class productTemplate(models.Model):
    _name= "product.template"
    _inherit = "product.template"
    
    codice_prodotto_sam = fields.Char(string = "Codice prodotto SAM", store = True)
    
    tipo_articolo = fields.Selection([("componente", "Componente"), ("insieme", "Insieme"), ("servizio", "Servizio"), 
                                      ("sottoinsieme", "Sottoinsieme"), ("commento", "Commento"), ("intervento", "Intervento")], string = "Tipo Articolo", store = True)
    
    codice_merce = fields.Char(string = "Codice Merce", store = True)
    descrizione_nomenclatura_combinata = fields.Char(string = "Descrizione nomenclatura combinata", store = True)
    
    tipo_produzione_articolo = fields.Selection([("commerciale", "Commerciale"), ("fantasma", "Fantasma"), 
                                                 ("interno", "Interno"), ("esterno", "Esterno")], string = "Tipo produzione articolo", store = True)
    
    stato_articolo = fields.Selection([("gestito", "Gestito"), ("installabile", "Installabile"), ("superato", "Superato"),], string = "Stato articolo", store = True)
    
    matricola = fields.Char(string = "Matricola", store = True, copy = True)
    
    
class productProduct(models.Model):
    _name ="product.product"
    _inherit = "product.product"
    
    codice_prodotto_sam = fields.Char(string = "Codice prodotto SAM", related="product_tmpl_id.codice_prodotto_sam", store = True, readonly = False)
    
    tipo_articolo = fields.Selection([("componente", "Componente"), ("insieme", "Insieme"), ("servizio", "Servizio"), 
                                      ("sottoinsieme", "Sottoinsieme"), ("commento", "Commento"), ("intervento", "Intervento")], string = "Tipo Articolo",  related="product_tmpl_id.tipo_articolo", store = True, readonly = False)
    
    codice_merce = fields.Char(string = "Codice Merce", related="product_tmpl_id.codice_merce", store = True, readonly = False)
    descrizione_nomenclatura_combinata = fields.Char(string = "Descrizione nomenclatura combinata", related="product_tmpl_id.descrizione_nomenclatura_combinata", store = True, readonly = False)
    
    tipo_produzione_articolo = fields.Selection([("commerciale", "Commerciale"), ("fantasma", "Fantasma"), 
                                                 ("interno", "Interno"), ("esterno", "Esterno")], string = "Tipo produzione articolo", related="product_tmpl_id.tipo_produzione_articolo", store = True, readonly = False)
    
    stato_articolo = fields.Selection([("gestito", "Gestito"), ("installabile", "Installabile"), ("superato", "Superato"),], string = "Stato articolo", related="product_tmpl_id.stato_articolo", store = True, readonly = False)
    
    matricola = fields.Char(string = "Matricola", store = True, related="product_tmpl_id.matricola", copy = True, readonly = False)
