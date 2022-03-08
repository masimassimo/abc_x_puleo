# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)


class abc_campi_product_template(models.Model):
    _name = 'abc_campi_product_template.abc_campi_product_template'
    _description = 'abc_campi_product_template.abc_campi_product_template'

class productTemplate(models.Model):
    _name= "product.template"
    _inherit = "product.template"
    
    codice_prodotto_sam = fields.Char(string = "Codice prodotto SAM", store = True)
    
    tipo_articolo = fields.Selection([("componente", "Componente"), ("insieme", "Insieme"), ("servizio", "Servizio"), 
                                      ("sottoinsieme", "Sottoinsieme"), ("commento", "Commento"), ("intervento", "Intervento")], string = "Tipo Articolo", store = True)
    
    codice_merce = fields.Char(string = "Nomenclatura Combinata", store = True)
    descrizione_nomenclatura_combinata = fields.Char(string = "Descrizione nomenclatura combinata", store = True)
    
    tipo_produzione_articolo = fields.Selection([("commerciale", "Commerciale"), ("fantasma", "Fantasma"), 
                                                 ("interno", "Interno"), ("esterno", "Esterno")], string = "Tipo produzione articolo", store = True)
    
    stato_articolo = fields.Selection([("gestito", "Gestito"), ("installabile", "Installabile"), ("superato", "Superato"),], string = "Stato articolo", store = True)
    
    #matricola = fields.Many2one(related="product_variant_id.matricola", string = "Matricola", store = True, copy = True, readonly = False)
    
    

    
class productProduct(models.Model):
    _name ="product.product"
    _inherit = "product.product"
    
    codice_prodotto_sam = fields.Char(string = "Codice prodotto SAM", related="product_tmpl_id.codice_prodotto_sam", store = True, readonly = False)
    
    tipo_articolo = fields.Selection([("componente", "Componente"), ("insieme", "Insieme"), ("servizio", "Servizio"), 
                                      ("sottoinsieme", "Sottoinsieme"), ("commento", "Commento"), ("intervento", "Intervento")], string = "Tipo Articolo",  related="product_tmpl_id.tipo_articolo", store = True, readonly = False)
    
    codice_merce = fields.Char(string = "Nomenclatura Combinata", related="product_tmpl_id.codice_merce", store = True, readonly = False)
    descrizione_nomenclatura_combinata = fields.Char(string = "Descrizione nomenclatura combinata", related="product_tmpl_id.descrizione_nomenclatura_combinata", store = True, readonly = False)
    
    tipo_produzione_articolo = fields.Selection([("commerciale", "Commerciale"), ("fantasma", "Fantasma"), 
                                                 ("interno", "Interno"), ("esterno", "Esterno")], string = "Tipo produzione articolo", related="product_tmpl_id.tipo_produzione_articolo", store = True, readonly = False)
    
    stato_articolo = fields.Selection([("gestito", "Gestito"), ("installabile", "Installabile"), ("superato", "Superato"),], string = "Stato articolo", related="product_tmpl_id.stato_articolo", store = True, readonly = False)
    
    matricola = fields.Many2many('stock.production.lot', string = "Matricola", store = True, domain= " [('product_id', '=', id)] ", copy = True, readonly = False)
    
    #matricola2= fields.Many2one('stock.production.lot', string = "matricola_2", domain= " [('product_id', '=', id)] ", readonly=False)
    

class accountMoveLine(models.Model):
    _name = "account.move.line"
    _inherit = "account.move.line"
    
    matricola = fields.Many2many('stock.production.lot', string = "Matricola", store = True, domain= " [('product_id', '=', product_id)] ", copy = True, readonly = False)    

class stockProductionLot(models.Model):
    _name = 'stock.production.lot'
    _inherit = "stock.production.lot"
    
    righe_fattura = fields.One2many('account.move.line', 'matricola', string="Righe Fattura", readonly = True)


