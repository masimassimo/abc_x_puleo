# -*- coding: utf-8 -*-
{
    'name': "ABC - CMR",

    'summary': """
        Modulo per la stampa del modello MRC Convention Relative au Contrat de Transport International de Marchandises par la Route""",

    'description': """
        Modulo per la stampa del modello MRC Convention Relative au Contrat de Transport International de Marchandises par la Route
    """,

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",
    
    'category': 'Inventory',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['stock','web', 'base'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        'data/cmr_paperformat.xml',
        'views/report_cmr.xml',
        'views/stock_picking_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    "installable": True,
    "application": True,
}
