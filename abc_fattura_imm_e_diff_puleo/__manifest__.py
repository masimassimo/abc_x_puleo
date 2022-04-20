# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_fattura_imm_e_diff_puleo",

    'summary': """Modulo che permette di generare la fattura immediata o differita per Puleo.""",

    'description': """Modulo che permette di generare la fattura immediata o differita per Puleo.""",

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Account',
    'version': '1.5',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'data/fattura_formato_carta.xml',
        'report/fattura_imm_e_diff_puleo.xml',

    ],
    'application': True,
    'installable': True,
    # only loaded in demonstration mode
    'demo': [],
}
