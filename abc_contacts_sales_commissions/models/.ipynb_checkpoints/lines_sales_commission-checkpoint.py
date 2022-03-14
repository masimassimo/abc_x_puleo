# -*- coding: utf-8 -*-

from odoo import models, fields, api

class abc_lines_sales_commission(models.Model):
    _name = "abc.lines_sales_commission"
    _description = "Sotto modulo che gestisce le righe di provvigione relative ai vari ordini di vendita."