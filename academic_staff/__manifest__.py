{
    'name': 'Academic Staff Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage academic staff and their teaching loads',
    'depends': ['base','academic_department'],
    'data': [
        'security/ir.model.access.csv',
        'views/staff_load_views.xml',
        'views/staff_views.xml',
    ],
    'installable': True,
    'application': True,
}