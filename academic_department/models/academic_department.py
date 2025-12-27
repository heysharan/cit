from odoo import models, fields

class AcademicDepartment(models.Model):
    _name = 'academic.department'
    _description = 'Academic Department'

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code")

