# -*- coding: utf-8 -*-

from odoo import models, fields, api


class abc_campi_res_partner(models.Model):
    _name = 'abc_campi_res_partner.abc_campi_res_partner'
    _description = 'abc_campi_res_partner.abc_campi_res_partner'


class resPartner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    
    #cliente = fields.Boolean(string="Cliente", default = False, store=True)
    #fornitore = fields.Boolean(string="Fornitore", default = False, store=True)
    #banca = fields.Boolean(string="Banca", default = False, store=True)
    #vettore = fields.Boolean(string="Vettore", default = False, store=True)
    #agente = fields.Boolean(string="Agente", default = False, store=True)
    #dipendente = fields.Boolean(string="Dipendente", default = False, store=True)
    
    cliente_o_fornitore_id_sam = fields.Char(string = "Cliente/Fornitore ID SAM", store = True)
    persona_id_sam = fields.Char(string = "Persona ID SAM", store = True)
    codice_sam_contatti = fields.Char(string= "Codice SAM Contatti", store = True)
    
    codice_zona = fields.Char(string = "Codice zona", store = True)
    descrizione_zona = fields.Char(string = "Descrizione zona", store = True)
    
    fax = fields.Char(string = "FAX", store = True)
    
    codice_categoria_contatto = fields.Char(string = "Codice categoria contatto", store = True)
    descrizione_categoria_contatto = fields.Char(string = "Descrizione categoria contatto", store = True)
    
    agente_id = fields.Many2one('res.partner', string ='Agente ID', change_default=True, index=True)
    
    segnalatore_id = fields.Many2one('res.partner', string ='Segnalatore ID', change_default=True, index=True)
    
    codice_area = fields.Char(string = "Codice area", store = True)
    descrizione_area = fields.Char(string = "Descrizione area", store = True)
        
    codice_settore = fields.Char(string = "Codice settore", store = True)
    descrizione_settore = fields.Char(string = "Descrizione settore", store = True)
    
    funzione = fields.Char(string = "Funzione", store = True)
    tipologia = fields.Char(string = "Tipologia", store = True)
    
    id_lead = fields.Char(string = "ID Lead", store = True)
