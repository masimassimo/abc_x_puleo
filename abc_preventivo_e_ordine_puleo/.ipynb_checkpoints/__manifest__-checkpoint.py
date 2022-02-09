# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_preventivo_e_ordine_puleo",

    'summary': """Modulo di stampa personalizzato Puleo per Preventivo / Ordine di vendita.""",

    'description': """Modulo di stampa personalizzato Puleo per Preventivo / Ordine di vendita.""",

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/preventivo_e_ordine_formato_carta.xml',
        'report/preventivo_e_ordine_puleo.xml',

    ],
    "installable":True,
    "application":True,

    'demo': [],
}
