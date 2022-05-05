# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class abc_payments_forecast(models.Model):
    _name = 'abc_payments_forecast.abc_payments_forecast'
    _description = 'Payments Forecast'

    name = fields.Char()
    value = fields.Float('Unit Price', required=True, digits='Product Price', default=0.0)
    percentage = fields.Float('Percentage', digits=(3,2) , default=0.0)
    #modalita = fields.Selection([('cash', 'Cash'),('bank', 'Bank')], string="Payment")
    tipologia = fields.Many2one('abc_payments_forecast.abc_payments_forecast_tipologie', string="Type")
    #metodo = fields.Many2one('abc_payments_forecast.abc_payments_forecast_metodi', string="Method")
    metodo = fields.Many2one('account.payment.term', string="Method")
    date = fields.Date()
    sale_order_id = fields.Many2one("sale.order", ondelete='set null')
    fatture = fields.Many2many('account.move', string="Fatture")
    cliente = fields.Many2one('res.partner', string="Cliente", compute='_compila_cliente', store=True)
    
    @api.onchange('percentage')
    def onchange_percentage(self):
        for record in self:
            total = record.sale_order_id.amount_total
            record.value = total * record.percentage / 100
    
    @api.constrains('percentage')
    def _check_percentage(self):
        for record in self:
            if record.percentage < 0 or record.percentage > 100:
                raise ValidationError("Invalid percentage value (" + str(record.percentage) + ") on payments forecast, it must be between 0 and 100.")
                
    @api.depends('sale_order_id')
    def _compila_cliente(self):
        for record in self:
            record.cliente = record.sale_order_id.partner_id
        
class AccountMove(models.Model):
    _name = "account.move"
    _inherit = "account.move"
    
    payment_forecast_ids = fields.Many2many('abc_payments_forecast.abc_payments_forecast', string="Fatture")
        
class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = "sale.order"
    
    payment_forecast_ids = fields.One2many(comodel_name="abc_payments_forecast.abc_payments_forecast",inverse_name='sale_order_id')
    
    @api.onchange('partner_id','payment_forecast_ids')
    def _check_cliente_linee(self):
        for record in self:
            for linea in record.payment_forecast_ids:
                linea['cliente'] = record.partner_id
                linea['sale_order_id'] = record.id
    
class abc_payments_forecast_tipologie(models.Model):
    _name = 'abc_payments_forecast.abc_payments_forecast_tipologie'
    _description = 'Tipologie di Pagamento'

    name = fields.Char()
    description = fields.Text()
    
class abc_payments_forecast_metodi(models.Model):
    _name = 'abc_payments_forecast.abc_payments_forecast_metodi'
    _description = 'Metodi di Pagamento'

    name = fields.Char()
    description = fields.Text()
