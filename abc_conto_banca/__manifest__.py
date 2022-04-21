# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_conto_banca",

    'summary': """Modulo che aggiunge il campo Banca, nell'Ordine di Vendita, il quale permette di ottenere la banca e il numero del conto relativi a quelli della propria azienda. Questo campo sarà anche stampato nel pdf.""",

    'description': """
        Modulo che aggiunge il campo Banca, nell'Ordine di Vendita, il quale permette di ottenere la banca e il numero del conto relativi a quelli della propria azienda. Questo campo sarà anche stampato nel pdf.""",

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Sale',
    'version': '0.4',

    'depends': ['base', 'sale', 'account', 'account_bank_statement_import', 'base_iban', 'account_qr_code_sepa'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    "installable": True,
    "application": True,
    'demo': [],
}
