# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_contacts_sales_commissions",

    'summary': """ Modulo che permette di gestire le provvigioni sui contatti. """,

    'description': """ Modulo che permette di gestire le provvigioni sui contatti. """,

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Contacts',
    'version': '0.9',

    'depends': ['base', 'account', 'sale'],

    'data': [
        'security/ir.model.access.csv',
        'views/abc_contacts_sales_commissions.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/abc_lines_sales_commission.xml',
        'views/account_move.xml',
        'views/conf.xml',
        'data/sequence.xml',
        'wizard/wizard_report_provvigioni_view.xml',
        'data/report_provvigioni_formato_carta.xml',
        'report/report_provvigioni_conf.xml',
        'report/report_provvigioni_pdf.xml',
    ],
    "installable": True,
    "application": True,
    'demo': [],
}
