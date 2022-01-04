# -*- coding: utf-8 -*-
# from odoo import http


# class ProductExtension(http.Controller):
#     @http.route('/product_extension/product_extension/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_extension/product_extension/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_extension.listing', {
#             'root': '/product_extension/product_extension',
#             'objects': http.request.env['product_extension.product_extension'].search([]),
#         })

#     @http.route('/product_extension/product_extension/objects/<model("product_extension.product_extension"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_extension.object', {
#             'object': obj
#         })
