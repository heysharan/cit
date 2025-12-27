from odoo import http
from odoo.http import request
import io
import xlsxwriter

class AcademicReportExcel(http.Controller):

    @http.route('/academic_reports/excel/<int:wizard_id>', type='http', auth='user')
    def export_excel(self, wizard_id):
        wizard = request.env['academic.report.wizard'].browse(wizard_id)

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        sheet = workbook.add_worksheet('Academic Report')

        sheet.write(0, 0, 'Department')
        sheet.write(0, 1, wizard.department_id.name)
        sheet.write(1, 0, 'Academic Year')
        sheet.write(1, 1, wizard.academic_year)

        workbook.close()
        output.seek(0)

        return request.make_response(
            output.read(),
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', 'attachment; filename=academic_report.xlsx')
            ]
        )
