# -*- coding: utf-8 -*-
# from odoo import http


# class AbcCustomHeaderPuleo(http.Controller):
#     @http.route('/abc_custom_header_puleo/abc_custom_header_puleo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_custom_header_puleo/abc_custom_header_puleo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_custom_header_puleo.listing', {
#             'root': '/abc_custom_header_puleo/abc_custom_header_puleo',
#             'objects': http.request.env['abc_custom_header_puleo.abc_custom_header_puleo'].search([]),
#         })

#     @http.route('/abc_custom_header_puleo/abc_custom_header_puleo/objects/<model("abc_custom_header_puleo.abc_custom_header_puleo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_custom_header_puleo.object', {
#             'object': obj
#         })
