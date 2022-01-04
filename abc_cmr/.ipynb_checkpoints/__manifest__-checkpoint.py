# -*- coding: utf-8 -*-
{
    'name': "abc_cmr",

    'summary': """
        Modulo per la stampa del modello MRC Convention Relative au Contrat de Transport International de Marchandises par la Route""",

    'description': """
        Modulo per la stampa del modello MRC Convention Relative au Contrat de Transport International de Marchandises par la Route
    """,

    'author': "Massimo Masi - ABC Srl",
    'website': "http://www.abcstrategie.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'stock',
        'web'
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/cmr_paperformat.xml',
        'views/report_cmr.xml',
        'views/stock_picking_view.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
}
