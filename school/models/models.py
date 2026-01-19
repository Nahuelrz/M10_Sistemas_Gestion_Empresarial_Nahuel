# -*- coding: utf-8 -*-

from odoo import models, fields, api


class student(models.Model):
    _name = 'school.student'
    _description = 'school.student'

    name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    dni = fields.Char(required=True)
    birthdate = fields.Date()
    active = fields.Boolean(default=True)
    age = fields.Integer()
    
    class_id = fields.Many2one('school.class')
    event_ids = fields.Many2many('school.event')
    
    _sql_constraints = [
        ('dni_unique', 'UNIQUE(dni)', 'El DNI debe ser único')
    ]


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

    name = fields.Char()
    state = fields.Date()
    type = fields.Selection([('allowance', 'Permiso'), ('delay', 'Retraso'), ('congratulations', 'Felicitaciones'), ('behavior', 'Comportamiento')])
    description = fields.Text()
    
    student_ids = fields.Many2many('school.student')

