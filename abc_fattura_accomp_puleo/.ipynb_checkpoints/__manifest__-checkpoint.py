# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_fattura_accomp_puleo",

    'summary': """ Modulo che permette di generare il report della fattura accompagnatoria. """,

    'description': """ Modulo che permette di generare il report della fattura accompagnatoria. """,

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Account',
    'version': '0.1',

    'depends': ['base', 'account', 'sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/fattura_accomp_formato_carta.xml',
        'report/fattura_accomp_puleo.xml',
    ],
    "installable": True,
    "application": True,
    'demo': [],
}
