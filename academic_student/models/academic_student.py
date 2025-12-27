from odoo import models, fields


class AcademicStudent(models.Model):
    _name = 'academic.student'
    _description = 'Academic Student'
    _rec_name = 'roll_no'

    roll_no = fields.Char(string='Roll No', required=True)
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name')

    dob = fields.Date(string='Date of Birth')

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')

    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')

    year_of_joining = fields.Integer(string='Year of Joining')

    year = fields.Selection([
        ('2', 'II'),
        ('3', 'III')
    ], string='Year')

    status = fields.Selection([
        ('active', 'Active'),
        ('graduated', 'Graduated')
    ], string='Status', default='active')

    department_id = fields.Many2one(
        'academic.department',
        string='Department',
        required=True
    )
