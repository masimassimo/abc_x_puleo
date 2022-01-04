# -*- coding: utf-8 -*-
# from odoo import http


# class AbcCmr(http.Controller):
#     @http.route('/abc_cmr/abc_cmr/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_cmr/abc_cmr/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_cmr.listing', {
#             'root': '/abc_cmr/abc_cmr',
#             'objects': http.request.env['abc_cmr.abc_cmr'].search([]),
#         })

#     @http.route('/abc_cmr/abc_cmr/objects/<model("abc_cmr.abc_cmr"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_cmr.object', {
#             'object': obj
#         })
