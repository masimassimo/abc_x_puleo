# -*- coding: utf-8 -*-
# from odoo import http


# class AbcNoEditProducts(http.Controller):
#     @http.route('/abc_no_edit_products/abc_no_edit_products/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_no_edit_products/abc_no_edit_products/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_no_edit_products.listing', {
#             'root': '/abc_no_edit_products/abc_no_edit_products',
#             'objects': http.request.env['abc_no_edit_products.abc_no_edit_products'].search([]),
#         })

#     @http.route('/abc_no_edit_products/abc_no_edit_products/objects/<model("abc_no_edit_products.abc_no_edit_products"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_no_edit_products.object', {
#             'object': obj
#         })
