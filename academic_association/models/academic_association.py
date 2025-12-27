from odoo import models, fields

class AcademicAssociation(models.Model):
    _name = 'academic.association'
    _description = 'Academic Association'

    name = fields.Char(required=True)
    department_id = fields.Many2one('academic.department', required=True)
    faculty_incharge = fields.Many2one('academic.staff', required=True)
    role_name = fields.Selection([
        ('president', 'President'),
        ('secretary', 'Secretary'),
        ('member', 'Member')
    ], required=True)

    event_ids = fields.One2many(
        'academic.association.event', 'association_id', string="Events"
    )
