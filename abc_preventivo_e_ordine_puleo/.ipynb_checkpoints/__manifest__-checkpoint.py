# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_preventivo_e_ordine_puleo",

    'summary': """Modulo di stampa personalizzato Puleo per Preventivo / Ordine di vendita e di acquisto. Fattura PRO FORMA inclusa.""",

    'description': """Modulo di stampa personalizzato Puleo per Preventivo / Ordine di vendita e di acquisto. Fattura PRO FORMA inclusa.""",

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Sale',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'purchase', 'purchase_order_secondary_unit', 'product_secondary_unit'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/preventivo_e_ordine_formato_carta.xml',
        'data/preventivo_e_ordine_formato_carta_acquisto.xml',
        'report/preventivo_e_ordine_puleo.xml',
        'report/preventivo_acquisto_puleo.xml',
        'report/acquisto_print_report.xml',
        'report/ordine_acquisto_puleo.xml',
        'report/fattura_pro_forma_puleo.xml',

    ],
    "installable":True,
    "application":True,

    'demo': [],
}
