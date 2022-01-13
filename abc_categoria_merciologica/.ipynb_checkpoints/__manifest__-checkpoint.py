# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_categoria_merciologica",

    'summary': """Modulo che aggiunge il campo categoria_merciologica alle Categorie Prodotto""",

    'description': """Modulo che aggiunge il campo categoria_merciologica alle Categorie Prodotto""",

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Product',
    'version': '0.1',

    'depends': ['base', "product"],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    "installable": True,
    "applicatiom": True,
    
    'demo': [],
}
