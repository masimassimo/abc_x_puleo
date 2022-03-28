from odoo import models, fields, api, _

class abc_report_provvigioni(models.TransientModel):
    _name = "abc.report_provvigioni"
    
    #Contatto al quale si vuole dare la provvigione.
    contatto = fields.Many2one("res.partner", string = "Contatto", help = "Contatto al quale si desidera dare la provvigione.", tracking = True, required = True, store = True)