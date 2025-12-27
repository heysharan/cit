{
    'name': 'Academic Student Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Student Management Module',
    'depends': ['base', 'academic_department'],
    'data': [
        'security/ir.model.access.csv',
        'views/academic_student_views.xml',
    ],
    'installable': True,
    'application': True,
}
