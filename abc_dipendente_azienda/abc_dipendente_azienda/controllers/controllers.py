# -*- coding: utf-8 -*-
# from odoo import http


# class AbcDipendenteAzienda(http.Controller):
#     @http.route('/abc_dipendente_azienda/abc_dipendente_azienda/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_dipendente_azienda/abc_dipendente_azienda/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_dipendente_azienda.listing', {
#             'root': '/abc_dipendente_azienda/abc_dipendente_azienda',
#             'objects': http.request.env['abc_dipendente_azienda.abc_dipendente_azienda'].search([]),
#         })

#     @http.route('/abc_dipendente_azienda/abc_dipendente_azienda/objects/<model("abc_dipendente_azienda.abc_dipendente_azienda"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_dipendente_azienda.object', {
#             'object': obj
#         })
