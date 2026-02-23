# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class student(models.Model):
    _name = 'school.student'
    _description = 'school.student'

    name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    dni = fields.Char(required=True)
    birthdate = fields.Date()
    active = fields.Boolean(default=True)
    age = fields.Integer(compute='_compute_age')
    
    class_id = fields.Many2one('school.class')
    event_ids = fields.Many2many('school.event')
    
    _sql_constraints = [
        ('dni_unique', 'UNIQUE(dni)', 'El DNI debe ser único')
    ]

    @api.depends('birthdate')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.birthdate:
                record.age = today.year - record.birthdate.year - (
                    (today.month, today.day) < (record.birthdate.month, record.birthdate.day)
                )
            else:
                record.age = 0


class school_class(models.Model):
    _name = 'school.class'
    _description = 'school.class'

    name = fields.Char(required=True)
    grade = fields.Selection([('preschool', 'Preescolar'), ('second', 'Segundo'), ('third', 'Tercero'), ('fourth', 'Cuarto')])
    classroom = fields.Char()
    state_end = fields.Date()
    student_number = fields.Integer()
    description = fields.Text()
    
    teacher_id = fields.Many2one('hr.employee')
    student_ids = fields.One2many('school.student', 'class_id')


class event(models.Model):
    _name = 'school.event'
    _description = 'school.event'
    _order = 'state desc'

    state = fields.Date()
    type = fields.Selection([('allowance', 'Permiso'), ('delay', 'Retraso'), ('congratulations', 'Felicitaciones'), ('behavior', 'Comportamiento')])
    description = fields.Text()
    
    classroom_id = fields.Many2one('school.class', string='Clase')
    student_ids = fields.Many2many('school.student')

    def name_get(self):
        result = []
        for record in self:
            type_label = dict(self._fields['type'].selection).get(record.type, '')
            classroom_name = record.classroom_id.name or ''
            name = "%s - %s" % (type_label, classroom_name)
            result.append((record.id, name))
        return result

