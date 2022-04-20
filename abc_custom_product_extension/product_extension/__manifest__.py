# -*- coding: utf-8 -*-
{
    'name': "ABC - Product Extension",

    'summary': """
        Il modulo product_extension permette di convertire il campo Descrizione vendite del Prodotto 
        da testo semplice in HTML.""",

    'description': """
        Il modulo product_extension permette di convertire il campo Descrizione vendite del Prodotto 
        da testo semplice in HTML. """,

    'author': "A.B.C. srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Product',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['product','sale', 'sale_management', 'purchase', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_product.xml',
        'views/view_sale.xml',
        'views/view_account.xml',
        'report/quotation_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'application': True,
}
