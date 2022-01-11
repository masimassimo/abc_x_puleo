# -*- coding: utf-8 -*-

from odoo import models, fields, api


class abc_campi_res_partner(models.Model):
    _name = 'abc_campi_res_partner.abc_campi_res_partner'
    _description = 'abc_campi_res_partner.abc_campi_res_partner'
    #TEST


class resPartner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    
    cliente = fields.Boolean(string="Cliente", default = False, store=True)
    fornitore = fields.Boolean(string="Fornitore", default = False, store=True)
    banca = fields.Boolean(string="Banca", default = False, store=True)
    vettore = fields.Boolean(string="Vettore", default = False, store=True)
    agente = fields.Boolean(string="Agente", default = False, store=True)
    dipendente = fields.Boolean(string="Dipendente", default = False, store=True)
    
    zona = fields.Char(string = "Zona", store = True)

    #leve_emozionali = fields.Text(string = "Leve emozionali", store = True)
    
