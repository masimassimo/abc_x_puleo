# -*- coding: utf-8 -*-
# from odoo import http


# class AbcReportBarcode(http.Controller):
#     @http.route('/abc_report_barcode/abc_report_barcode/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_report_barcode/abc_report_barcode/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_report_barcode.listing', {
#             'root': '/abc_report_barcode/abc_report_barcode',
#             'objects': http.request.env['abc_report_barcode.abc_report_barcode'].search([]),
#         })

#     @http.route('/abc_report_barcode/abc_report_barcode/objects/<model("abc_report_barcode.abc_report_barcode"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_report_barcode.object', {
#             'object': obj
#         })
