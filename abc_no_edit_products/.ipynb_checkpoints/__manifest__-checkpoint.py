# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_no_edit_products",

    'summary': """
        Modulo che disabilita la creazione dei prodotti.""",

    'description': """
        Modulo che disabilita la creazione dei prodotti.
    """,

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    "installable": True,
    "application": True,
    # only loaded in demonstration mode
    'demo': [],
}
