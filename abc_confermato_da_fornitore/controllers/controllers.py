# -*- coding: utf-8 -*-
# from odoo import http


# class AbcConfermatoDaFornitore(http.Controller):
#     @http.route('/abc_confermato_da_fornitore/abc_confermato_da_fornitore/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_confermato_da_fornitore/abc_confermato_da_fornitore/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_confermato_da_fornitore.listing', {
#             'root': '/abc_confermato_da_fornitore/abc_confermato_da_fornitore',
#             'objects': http.request.env['abc_confermato_da_fornitore.abc_confermato_da_fornitore'].search([]),
#         })

#     @http.route('/abc_confermato_da_fornitore/abc_confermato_da_fornitore/objects/<model("abc_confermato_da_fornitore.abc_confermato_da_fornitore"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_confermato_da_fornitore.object', {
#             'object': obj
#         })
