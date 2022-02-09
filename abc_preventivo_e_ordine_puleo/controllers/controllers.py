# -*- coding: utf-8 -*-
# from odoo import http


# class AbcPreventivoEOrdinevenditaPuleo(http.Controller):
#     @http.route('/abc_preventivo_e_ordinevendita_puleo/abc_preventivo_e_ordinevendita_puleo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_preventivo_e_ordinevendita_puleo/abc_preventivo_e_ordinevendita_puleo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_preventivo_e_ordinevendita_puleo.listing', {
#             'root': '/abc_preventivo_e_ordinevendita_puleo/abc_preventivo_e_ordinevendita_puleo',
#             'objects': http.request.env['abc_preventivo_e_ordinevendita_puleo.abc_preventivo_e_ordinevendita_puleo'].search([]),
#         })

#     @http.route('/abc_preventivo_e_ordinevendita_puleo/abc_preventivo_e_ordinevendita_puleo/objects/<model("abc_preventivo_e_ordinevendita_puleo.abc_preventivo_e_ordinevendita_puleo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_preventivo_e_ordinevendita_puleo.object', {
#             'object': obj
#         })
