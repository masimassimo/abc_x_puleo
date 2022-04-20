# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _name = "purchase.order"
    _inherit = "purchase.order"

    confermato_da_fornitore = fields.Boolean(string="Confermato da fornitore")
    data_ordine_acquisto = fields.Date(string="Data ordine di acquisto")
    
    def write(self, values):
        for record in self:
            if 'state' in values:
                #raise UserError(values.list))
                if record.state != 'purchase' and values['state'] == 'purchase':
                    values['data_ordine_acquisto'] = fields.Date.today()
                    
        return super(PurchaseOrder, self).write(values)
    
    def verifica_scadenza_conferma(self):
        for record in self:
            if record.state == 'purchase' and record.data_ordine_acquisto != False:
                current_date = datetime.datetime.now().date()
                if (current_date-datetime.timedelta(days=3)) == record.data_ordine_acquisto:
                    data = {
                        'res_id': record.id,
                        'res_model_id': self.env['ir.model'].search([('model', '=', 'purchase.order')]).id,
                        'user_id': record.user_id.id,
                        'summary': 'Verifica conferma ODA ' + record.name,
                        'activity_type_id': 4,
                        'date_deadline': current_date
                        }
                    self.env['mail.activity'].create(data)
                    #raise UserError(record.name)
    
# class abc_confermato_da_fornitore(models.Model):
#     _name = 'abc_confermato_da_fornitore.abc_confermato_da_fornitore'
#     _description = 'abc_confermato_da_fornitore.abc_confermato_da_fornitore'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
