# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_report_barcode",

    'summary': """ Modulo che modifica il report di stampa del Barcode e dell'etichetta prodotto. """,

    'description': """ Modulo che modifica il report di stampa del Barcode e dell'etichetta prodotto. """,

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Products',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/formato_carta_barcode.xml',
        'report/codice_a_barre_prodotto.xml',
        'report/print_codice_a_barre_prodotto.xml',
        'report/etichetta_prodotto.xml',
        'report/print_etichetta_prodotto.xml',
    ],
    "installable": True,
    "application": True,
    'demo': [],
}
