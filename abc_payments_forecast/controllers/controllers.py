# -*- coding: utf-8 -*-
# from odoo import http


# class AbcPaymentsForecast(http.Controller):
#     @http.route('/abc_payments_forecast/abc_payments_forecast/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/abc_payments_forecast/abc_payments_forecast/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('abc_payments_forecast.listing', {
#             'root': '/abc_payments_forecast/abc_payments_forecast',
#             'objects': http.request.env['abc_payments_forecast.abc_payments_forecast'].search([]),
#         })

#     @http.route('/abc_payments_forecast/abc_payments_forecast/objects/<model("abc_payments_forecast.abc_payments_forecast"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('abc_payments_forecast.object', {
#             'object': obj
#         })
