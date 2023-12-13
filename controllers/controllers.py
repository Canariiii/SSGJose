# -*- coding: utf-8 -*-
# from odoo import http


# class Proyectojoel(http.Controller):
#     @http.route('/proyectojoel/proyectojoel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ssgjose/ssgjose/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ssgjose.listing', {
#             'root': '/ssgjose/ssgjose',
#             'objects': http.request.env['ssgjose.ssgjose'].search([]),
#         })

#     @http.route('/ssgjose/ssgjose/objects/<model("ssgjose.ssgjose"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ssgjose.object', {
#             'object': obj
#         })
