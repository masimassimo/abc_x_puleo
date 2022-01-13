# -*- coding: utf-8 -*-
# from odoo import http


# class AbcCategoriaMerciologica(http.Controller):
#     @http.route('/abc_categoria_merciologica/abc_categoria_merciologica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_categoria_merciologica/abc_categoria_merciologica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_categoria_merciologica.listing', {
#             'root': '/abc_categoria_merciologica/abc_categoria_merciologica',
#             'objects': http.request.env['abc_categoria_merciologica.abc_categoria_merciologica'].search([]),
#         })

#     @http.route('/abc_categoria_merciologica/abc_categoria_merciologica/objects/<model("abc_categoria_merciologica.abc_categoria_merciologica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_categoria_merciologica.object', {
#             'object': obj
#         })
