# -*- coding: utf-8 -*-
{
    'name': "ABC - Nominativo di riferimento",

    'summary': """
        Modulo che estende la vista del sale.view_order_form e permette l'aggiunta di un
        campo relazionale il quale in base al Cliente selezionato ti permette di scegliere
        un dipendente della stessa Azienda.""",

    'description': """
        Modulo che estende la vista del sale.view_order_form e permette l'aggiunta di un
        campo relazionale il quale in base al Cliente selezionato ti permette di scegliere
        un dipendente della stessa Azienda.
    """,

    'author': "A.B.C. Strategie",
    'website': "https://www.abcstrategie.it/",

    'category': 'Sale',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'report/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    "installable": True,
    "application": True,
}
