{
    'name': 'Academic Subjects / Curriculum',
    'version': '1.0',
    'summary': 'Manage subjects and curriculum',
    'category': 'Education',
    'author': 'Your Name',
    'license': 'LGPL-3',
    'depends': ['academic_department'],
    'data': [
        'security/ir.model.access.csv',
        'views/subject_views.xml',
    ],
    'installable': True,
    'application': True,
}
