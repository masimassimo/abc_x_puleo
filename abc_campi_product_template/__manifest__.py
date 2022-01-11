# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_campi_product_template",

    'summary': """Modulo contente i campi aggiunti nelle anagrafiche prodotti.""",

    'description': """
       Modulo contente i campi aggiunti nelle anagrafiche prodotti.
    """,

    'author': "A.B.C. srl",
    'website': "https://www.abcstrategie.it/",
    
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', "product"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
}
