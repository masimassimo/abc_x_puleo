# -*- coding: utf-8 -*-
# from odoo import http


# class AbcDdtPuleo(http.Controller):
#     @http.route('/abc_ddt_puleo/abc_ddt_puleo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_ddt_puleo/abc_ddt_puleo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_ddt_puleo.listing', {
#             'root': '/abc_ddt_puleo/abc_ddt_puleo',
#             'objects': http.request.env['abc_ddt_puleo.abc_ddt_puleo'].search([]),
#         })

#     @http.route('/abc_ddt_puleo/abc_ddt_puleo/objects/<model("abc_ddt_puleo.abc_ddt_puleo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_ddt_puleo.object', {
#             'object': obj
#         })
