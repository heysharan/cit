from odoo import models, fields

class AcademicStaffLoad(models.Model):
    _name = 'academic.staff.load'
    _description = 'Staff Teaching Load'
    _rec_name = 'course_name'

    staff_id = fields.Many2one(
        'academic.staff',
        string='Staff',
        required=True,
        ondelete='cascade'
    )

    course_name = fields.Char(
        string='Course / Paper',
        required=True
    )

    hours_per_week = fields.Integer(
        string='Hours per Week'
    )
