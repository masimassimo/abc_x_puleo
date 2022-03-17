# -*- coding: utf-8 -*-
{
    'name': "ABC - Calcolo prezzo seconda UDM",

    'summary': """ ABC - Modulo per il calcolo del prezzo d'acquisto con la seconda unità di misura""",

    'description': """ Modulo per il calcolo del prezzo d'acquisto con la seconda unità di misura """,

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it",

    'category': 'Purchases',
    'version': '0.1',

    'depends': ['base','purchase','product_secondary_unit','purchase_order_secondary_unit'],

    'data': [
        'views/views.xml',
    ],
    "installable": True,
    "application": True,
    'demo': [],
}
