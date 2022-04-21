# -*- coding: utf-8 -*-
# from odoo import http


# class AbcDdtExpiration(http.Controller):
#     @http.route('/abc_ddt_expiration/abc_ddt_expiration/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_ddt_expiration/abc_ddt_expiration/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_ddt_expiration.listing', {
#             'root': '/abc_ddt_expiration/abc_ddt_expiration',
#             'objects': http.request.env['abc_ddt_expiration.abc_ddt_expiration'].search([]),
#         })

#     @http.route('/abc_ddt_expiration/abc_ddt_expiration/objects/<model("abc_ddt_expiration.abc_ddt_expiration"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_ddt_expiration.object', {
#             'object': obj
#         })
