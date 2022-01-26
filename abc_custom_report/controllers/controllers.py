# -*- coding: utf-8 -*-
# from odoo import http


# class AbcCustomReport(http.Controller):
#     @http.route('/abc_custom_report/abc_custom_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_custom_report/abc_custom_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_custom_report.listing', {
#             'root': '/abc_custom_report/abc_custom_report',
#             'objects': http.request.env['abc_custom_report.abc_custom_report'].search([]),
#         })

#     @http.route('/abc_custom_report/abc_custom_report/objects/<model("abc_custom_report.abc_custom_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_custom_report.object', {
#             'object': obj
#         })
