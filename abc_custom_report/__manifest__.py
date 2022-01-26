# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_custom_report",

    'summary': """Modulo che contiene tutte le modifiche fatte sui report di Puleo. (Fattura, Ordini di Vendita, Preventivi).""",

    'description': """Modulo che contiene tutte le modifiche fatte sui report di Puleo. (Fattura, Ordini di Vendita, Preventivi).""",

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",
    
    'category': 'Account',
    'version': '0.1',

    'depends': ['base', 'account'],

    'data': [
        'security/ir.model.access.csv',
        'report/custom_templates.xml',
    ],
    "application":True,
    "installable": True,

    'demo': [],
}
