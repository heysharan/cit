from odoo import models, fields

class AcademicPlacement(models.Model):
    _name = 'academic.placement'
    _description = 'Academic Placement'
    _rec_name = 'company_name'

    placement_id = fields.Char(string="Placement ID", required=True)
    company_name = fields.Char(string="Company Name", required=True)

    students_attended = fields.Integer(string="Students Attended")
    selected_round1 = fields.Integer(string="Selected – Round 1")
    selected_round2 = fields.Integer(string="Selected – Round 2")
    selected_final = fields.Integer(string="Final Selected")

    avg_salary = fields.Float(string="Average Salary (LPA)")
    highest_salary = fields.Float(string="Highest Salary (LPA)")

    acceptance_rate = fields.Float(
        string="Acceptance Rate (%)",
        compute="_compute_acceptance_rate",
        store=True
    )

    def _compute_acceptance_rate(self):
        for rec in self:
            if rec.students_attended:
                rec.acceptance_rate = (rec.selected_final / rec.students_attended) * 100
            else:
                rec.acceptance_rate = 0.0
