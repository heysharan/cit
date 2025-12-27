from odoo import models, fields


class AcademicStaff(models.Model):
    _name = 'academic.staff'
    _description = 'Academic Staff'

    name = fields.Char(string='Staff ID', required=True)
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    email = fields.Char()
    date_of_joining = fields.Date(default=fields.Date.context_today)
    qualification = fields.Char()
    designation = fields.Char()

    # Using many2one - assumes base department or your custom one
    department_id = fields.Many2one('academic.department', string='Department')

    profile_pdf = fields.Binary(string='Profile PDF')
    photo = fields.Binary(string='Photo')

    load_ids = fields.One2many('academic.staff.load', 'staff_id', string='Teaching Loads')