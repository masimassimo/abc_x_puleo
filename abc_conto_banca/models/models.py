# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class abc_conto_banca(models.Model):
    _name = 'abc_conto_banca.abc_conto_banca'
    _description = 'abc_conto_banca.abc_conto_banca'
    
#Eredito il modulo "SaleOrder" per accedere alla vista.
class SaleOrder(models.Model):
    _name = "sale.order"
    _inherit = 'sale.order'
    
    def _compute_bank(self):
        listaBanche = []
        puleo_id = self.env['res.partner'].search([['id','=',1]])
        banche_puleo_ids = puleo_id['bank_ids']
        for x in range(0, len(banche_puleo_ids)):
            #_logger.info(puleo_id['bank_ids'][x].bank_id.id)
            banca_name = banche_puleo_ids[x].bank_id.name
            banca_nConto = banche_puleo_ids[x].acc_number
            banca_bic = str(banche_puleo_ids[x].bank_id.bic)
            
            if(not banca_name):
                banca_name = "NULL"
            if(not banca_nConto):
                banca_nConto = "NULL"
            listaBanche.append((banca_name, banca_name + " - " + banca_nConto + " - BIC: " + banca_bic))
        return listaBanche

    banca = fields.Selection(selection=lambda self: self._compute_bank(), string='Banca di riferimento', store=True, required = True)
    
   
 
        
    banca_cliente = fields.Many2one("res.partner.bank", string = "Banca cliente", store = True, domain = "[('partner_id', '=', partner_id)]", copy = True)
