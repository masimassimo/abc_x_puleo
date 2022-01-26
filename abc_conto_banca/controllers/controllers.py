# -*- coding: utf-8 -*-
# from odoo import http


# class AbcContoBanca(http.Controller):
#     @http.route('/abc_conto_banca/abc_conto_banca/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_conto_banca/abc_conto_banca/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_conto_banca.listing', {
#             'root': '/abc_conto_banca/abc_conto_banca',
#             'objects': http.request.env['abc_conto_banca.abc_conto_banca'].search([]),
#         })

#     @http.route('/abc_conto_banca/abc_conto_banca/objects/<model("abc_conto_banca.abc_conto_banca"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_conto_banca.object', {
#             'object': obj
#         })
