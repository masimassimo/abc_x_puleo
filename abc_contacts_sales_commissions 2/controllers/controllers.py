# -*- coding: utf-8 -*-
# from odoo import http


# class AbcContactsSalesCommissions(http.Controller):
#     @http.route('/abc_contacts_sales_commissions/abc_contacts_sales_commissions/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_contacts_sales_commissions/abc_contacts_sales_commissions/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_contacts_sales_commissions.listing', {
#             'root': '/abc_contacts_sales_commissions/abc_contacts_sales_commissions',
#             'objects': http.request.env['abc_contacts_sales_commissions.abc_contacts_sales_commissions'].search([]),
#         })

#     @http.route('/abc_contacts_sales_commissions/abc_contacts_sales_commissions/objects/<model("abc_contacts_sales_commissions.abc_contacts_sales_commissions"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_contacts_sales_commissions.object', {
#             'object': obj
#         })
