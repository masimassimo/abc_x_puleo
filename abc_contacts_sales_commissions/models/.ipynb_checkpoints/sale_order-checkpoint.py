# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class saleOrder(models.Model):
    _inherit = "sale.order"
    _name = "sale.order"