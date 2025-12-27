from odoo import models, fields

class AcademicSubject(models.Model):
    _name = 'academic.subject'
    _description = 'Academic Subject'
    _rec_name = 'name'

    name = fields.Char(
        string='Subject Name',
        required=True
    )

    subject_code = fields.Char(
        string='Subject Code',
        required=True
    )

    department_id = fields.Many2one(
        'academic.department',
        string='Department',
        required=True,
        ondelete='restrict'
    )

    semester = fields.Selection(
        [
            ('1', 'I'),
            ('2', 'II'),
            ('3', 'III'),
            ('4', 'IV'),
            ('5', 'V'),
            ('6', 'VI'),
        ],
        string='Semester',
        required=True
    )

    subject_type = fields.Selection(
        [
            ('theory', 'Theory'),
            ('practical', 'Practical'),
            ('practicum', 'Practicum'),
        ],
        string='Subject Type',
        required=True
    )
