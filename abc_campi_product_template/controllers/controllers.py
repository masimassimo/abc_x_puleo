# -*- coding: utf-8 -*-
# from odoo import http


# class AbcCampiProductTemplate(http.Controller):
#     @http.route('/abc_campi_product_template/abc_campi_product_template/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_campi_product_template/abc_campi_product_template/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_campi_product_template.listing', {
#             'root': '/abc_campi_product_template/abc_campi_product_template',
#             'objects': http.request.env['abc_campi_product_template.abc_campi_product_template'].search([]),
#         })

#     @http.route('/abc_campi_product_template/abc_campi_product_template/objects/<model("abc_campi_product_template.abc_campi_product_template"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_campi_product_template.object', {
#             'object': obj
#         })
