from odoo import models, fields

class AcademicReportWizard(models.TransientModel):
    _name = 'academic.report.wizard'
    _description = 'Academic Report Wizard'

    department_id = fields.Many2one('academic.department', required=True)
    academic_year = fields.Char(required=True)
    report_type = fields.Selection(
        [('annual', 'Annual'), ('semester', 'Semester')],
        required=True
    )

    def action_generate_pdf(self):
        return self.env.ref('academic_reports.action_academic_report_pdf').report_action(self)

    def action_export_excel(self):
        return {
            'type': 'ir.actions.act_url',
            'url': '/academic_reports/excel/%s' % self.id,
            'target': 'self',
        }
