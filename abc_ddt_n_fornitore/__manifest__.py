# -*- coding: utf-8 -*-
{
    'name': "ABC numero DDT Fornitore",

    'summary': """
        Aggiunge il Riferimento del DDT del fornitore""",

    'description': """
        Aggiunge il Riferimento del DDT del fornitore
    """,

    'author': "Massimo Masi",
    'website': "https://www.abcstrategie.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Stock',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base','l10n_it_delivery_note', 'l10n_it_delivery_note_order_link', 'purchase', 'abc_confermato_da_fornitore'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
}
