# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_ddt_puleo",

    'summary': """ Modulo che modifica il template di base del DDT Puleo. """,

    'description': """ Modulo che modifica il template di base del DDT Puleo.  """,

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'DDT',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'l10n_it_delivery_note', 'l10n_it_delivery_note_batch', 'l10n_it_delivery_note_base', 'l10n_it_delivery_note_order_link'],

    # always loaded
    'data': [
        'data/ddt_formato_carta.xml',
        'security/ir.model.access.csv',
        'report/ddt_puleo.xml',
        'views/views.xml',
    ],
    "installable":True,
    "application": True,
    'demo': [],
}
