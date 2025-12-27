from odoo import models, fields

class AcademicAssociationEvent(models.Model):
    _name = 'academic.association.event'
    _description = 'Academic Association Event'

    association_id = fields.Many2one('academic.association', required=True, ondelete='cascade')
    event_no = fields.Char(required=True)
    event_date = fields.Date(required=True)
    event_name = fields.Char(required=True)
    event_report = fields.Binary()
    event_report_filename = fields.Char()
