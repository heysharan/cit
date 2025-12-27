{
    'name': 'Academic Association & Events',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage academic associations and events',
    'depends': ['base', 'academic_department', 'academic_staff'],
    'data': [
        'security/ir.model.access.csv',
        'views/placement_views.xml',
        'views/association_event_views.xml',
    ],
    'installable': True,
    'application': True,
}
