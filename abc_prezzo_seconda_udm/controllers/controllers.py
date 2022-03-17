# -*- coding: utf-8 -*-
# from odoo import http


# class AbcPrezzoSecondaUdm(http.Controller):
#     @http.route('/abc_prezzo_seconda_udm/abc_prezzo_seconda_udm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_prezzo_seconda_udm/abc_prezzo_seconda_udm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_prezzo_seconda_udm.listing', {
#             'root': '/abc_prezzo_seconda_udm/abc_prezzo_seconda_udm',
#             'objects': http.request.env['abc_prezzo_seconda_udm.abc_prezzo_seconda_udm'].search([]),
#         })

#     @http.route('/abc_prezzo_seconda_udm/abc_prezzo_seconda_udm/objects/<model("abc_prezzo_seconda_udm.abc_prezzo_seconda_udm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_prezzo_seconda_udm.object', {
#             'object': obj
#         })
