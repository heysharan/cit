{
    'name': 'Academic Attendance',
    'version': '1.0',
    'category': 'Academic',
    'summary': 'Manage attendance of students',
    'author': 'Your Name',
    'depends': ['academic_student'],  # parent module
    'data': [
        'security/ir.model.access.csv',
        'views/attendance_views.xml',
    ],
    'installable': True,
    'application': True,
}