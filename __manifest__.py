# -*- coding: utf-8 -*-
# author: 227Mahaman

{
    'name': 'Gestion de ibam',
    'version': '1.0',
    'category': 'Human Resources',
    'description': """
        gestion de la scolarité
        gestion des notes
    """,
    'website': '',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/filiere.xml'
        ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
