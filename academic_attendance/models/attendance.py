# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AcademicAttendance(models.Model):
    _name = 'academic.attendance'
    _description = 'Student Attendance'

    subject_id = fields.Many2one('academic.subject', string='Subject', required=True)
    student_id = fields.Many2one('academic.student', string='Student', required=True)
    month = fields.Selection([
        ('Jan','January'), ('Feb','February'), ('Mar','March'), ('Apr','April'),
        ('May','May'), ('Jun','June'), ('Jul','July'), ('Aug','August'),
        ('Sep','September'), ('Oct','October'), ('Nov','November'), ('Dec','December')],
        string='Month', required=True
    )
    hours_present = fields.Float(string='Hours Present', required=True)
    hours_total = fields.Float(string='Total Hours', required=True)
    percentage = fields.Float(string='Percentage', compute='_compute_percentage', store=True)
    status = fields.Selection([('present','Present'), ('absent','Absent'), ('late','Late')],
                              string='Status', default='present')

    @api.depends('hours_present', 'hours_total')
    def _compute_percentage(self):
        for rec in self:
            if rec.hours_total:
                rec.percentage = (rec.hours_present / rec.hours_total) * 100
            else:
                rec.percentage = 0

