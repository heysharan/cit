from odoo import models, fields

class AcademicInternalMark(models.Model):
    _name = "academic.internal.mark"
    _description = "Academic Internal Marks"
    _rec_name = "student_id"

    student_id = fields.Many2one(
        "academic.student",
        string="Student",
        required=True
    )

    subject_id = fields.Many2one(
        "academic.subject",
        string="Subject",
        required=True
    )

    year = fields.Selection(
        [
            ('2', 'II Year'),
            ('3', 'III Year'),
        ],
        string="Year",
        required=True
    )

    assessment_type = fields.Selection(
        [
            ('ca1', 'CA 1'),
            ('ca2', 'CA 2'),
            ('ca3', 'CA 3'),
            ('model', 'Model Exam'),
        ],
        string="Assessment Type",
        required=True
    )

    assignment_or_seminar_mark = fields.Integer(
        string="Assignment / Seminar Mark"
    )

    marks_obtained = fields.Integer(
        string="Marks Obtained",
        required=True
    )

    test_date = fields.Date(
        string="Test Date",
        required=True
    )

