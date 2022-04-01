# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class abc_contacts_sales_commissions_conf(models.TransientModel): 
    _inherit = 'res.config.settings'
    
    #Campo Booleano che permette di decidere se considerare gli Agenti di un determinato contatto o il solo Addetto Vendite.
    
    addetto_vendite = fields.Boolean(string = "Considera il solo Addetto vendite", help = "Campo Booleano che permette di decidere se considerare gli Agenti di un determinato contatto o il solo Addetto Vendite.", default = False)

    #indirizzo_ip_server = fields.Char( string = 'Indirizzo Ip Server', help="Indirizzo ip per collegare Odoo al server che gestisce le chiamate MQTT" ) 
        
    def get_values(self):
        res = super(abc_contacts_sales_commissions_conf, self).get_values()
        res.update(
            addetto_vendite=self.env['ir.config_parameter'].sudo().get_param('abc_contacts_sales_commissions.addetto_vendite')
        )
        return res

    def set_values(self):
        super(abc_contacts_sales_commissions_conf, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('abc_contacts_sales_commissions.addetto_vendite', self.addetto_vendite)