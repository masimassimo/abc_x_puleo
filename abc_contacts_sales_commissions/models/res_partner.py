# -*- coding: utf-8 -*-

from odoo import models, fields, api

class resPartner(models.Model):
    _inherit = "res.partner"
    _name = "res.partner"
    
    #Campo One2many collegato alla provvigione del contatto.
    provvigioni_ids = fields.One2many(comodel_name = "abc.contacts_sales_commissions", inverse_name = "contatto", string = "Provvigioni", help = "Specchietto provvigioni.", tracking = True)
    
    #Campo Many2many che si collega ai partner, NB: DIPENDE DA contatti_ids ALTRIMENTI NON FUNZIONA. 
    agenti_ids = fields.Many2many(comodel_name = "res.partner", relation = "relazione", column1 = "colonna1", column2 = "colonna2", string = "Agenti", domain = "[('provvigioni_ids', '!=', False)]")
    
    #Campo Many2many che si collega ai partner, NB: DIPENDE DA agenti_ids ALTRIMENTI NON FUNZIONA.
    contatti_ids = fields.Many2many(comodel_name = "res.partner", relation = "relazione", column1 = "colonna2", column2 = "colonna1", string = "Contatti associati", readonly = True)
    
    #Campo Booleano che permette di discriminare un cliente Direzionale da Non Direzionale.
    direzionale = fields.Boolean(string = "Direzionale", help = "Campo Booleano che permette di discriminare un cliente Direzionale da Non Direzionale.", tracking = True, default = False)