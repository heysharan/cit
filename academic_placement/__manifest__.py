{
    'name': 'Academic Placement Management',
    'version': '1.0',
    'category': 'Education',
    'summary': 'Manage campus placement records',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/placement_views.xml',
    ],
    'installable': True,
    'application': True,
}
