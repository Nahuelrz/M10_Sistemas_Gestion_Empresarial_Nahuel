# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class SchoolController(http.Controller):
    @http.route('/school/events/', auth='public', type='http')
    def list_events(self, **kw):
        events = request.env['school.event'].sudo().search([])
        event_names = events.name_get()
        result = "<h1>Lista de Eventos del Colegio</h1><ul>"
        for _id, name in event_names:
            result += "<li>%s</li>" % name
        result += "</ul>"
        return result

