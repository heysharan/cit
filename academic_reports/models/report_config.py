from odoo import models, fields

class AcademicReportConfig(models.Model):
    _name = 'academic.report.config'
    _description = 'Academic Report Configuration'

    department_id = fields.Many2one('academic.department', required=True)
    academic_year = fields.Char(required=True)
    report_type = fields.Selection(
        [('annual', 'Annual'), ('semester', 'Semester')],
        required=True
    )
