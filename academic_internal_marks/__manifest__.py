{
    'name': 'Academic Internal Marks',
    'version': '1.0',
    'depends': [
        'academic_student',
        'academic_subject',
        'academic_department'],
    'data': [
        'security/ir.model.access.csv',
        'views/internal_mark_views.xml',
    ],
    'installable': True,
    'application': False,
}

