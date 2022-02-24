# -*- coding: utf-8 -*-
# from odoo import http


# class AbcFatturaAccompPuleo(http.Controller):
#     @http.route('/abc_fattura_accomp_puleo/abc_fattura_accomp_puleo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_fattura_accomp_puleo/abc_fattura_accomp_puleo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_fattura_accomp_puleo.listing', {
#             'root': '/abc_fattura_accomp_puleo/abc_fattura_accomp_puleo',
#             'objects': http.request.env['abc_fattura_accomp_puleo.abc_fattura_accomp_puleo'].search([]),
#         })

#     @http.route('/abc_fattura_accomp_puleo/abc_fattura_accomp_puleo/objects/<model("abc_fattura_accomp_puleo.abc_fattura_accomp_puleo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_fattura_accomp_puleo.object', {
#             'object': obj
#         })
