# -*- coding: utf-8 -*-
{
    'name': "ABC - Campi_4_0",

    'summary': """Modulo contente i campi aggiunti per il 4.0.""",

    'description': """
        Modulo contente i campi aggiunti per il 4.0.
    """,

    'author': "A.B.C. srl",
    'website': "https://www.abcstrategie.it/",

   
    'category': 'Production',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mrp'],

    # always loaded
    'data': [
        'views/views.xml',
        'security/ir.model.access.csv',
    ],
    "installable": True,

    'demo': [],
}
