# -*- coding: utf-8 -*-
# from odoo import http


# class AbcCampiResPartner(http.Controller):
#     @http.route('/abc_campi_res_partner/abc_campi_res_partner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_campi_res_partner/abc_campi_res_partner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_campi_res_partner.listing', {
#             'root': '/abc_campi_res_partner/abc_campi_res_partner',
#             'objects': http.request.env['abc_campi_res_partner.abc_campi_res_partner'].search([]),
#         })

#     @http.route('/abc_campi_res_partner/abc_campi_res_partner/objects/<model("abc_campi_res_partner.abc_campi_res_partner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_campi_res_partner.object', {
#             'object': obj
#         })
