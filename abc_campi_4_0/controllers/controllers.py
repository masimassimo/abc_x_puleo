# -*- coding: utf-8 -*-
# from odoo import http


# class AbcCampi40(http.Controller):
#     @http.route('/abc_campi_4_0/abc_campi_4_0/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_campi_4_0/abc_campi_4_0/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_campi_4_0.listing', {
#             'root': '/abc_campi_4_0/abc_campi_4_0',
#             'objects': http.request.env['abc_campi_4_0.abc_campi_4_0'].search([]),
#         })

#     @http.route('/abc_campi_4_0/abc_campi_4_0/objects/<model("abc_campi_4_0.abc_campi_4_0"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_campi_4_0.object', {
#             'object': obj
#         })
