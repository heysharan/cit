{
    'name': 'Academic Reports',
    'version': '1.0',
    'category': 'Education',
    'depends': [
        'base',
        'academic_student',
        'academic_department',
        'academic_staff',
        'academic_attendance',
        'academic_placement',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/report_config_views.xml',
        'views/report_wizard_views.xml',
        'report/academic_report_template.xml',
    ],
    'application': True,
}
