# -*- coding: utf-8 -*-
{
    'name': "ABC - Campi res_partner",

    'summary': """Modulo contente i campi aggiunti nelle anagrafiche contatti.""",

    'description': """Modulo contente i campi aggiunti nelle anagrafiche contatti.""",

    'author': "A.B.C. srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Partners',
    'version': '0.4',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    "installable": True,
    "application": True,
    
    'demo': [],
}
