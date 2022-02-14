{
    'name': "ABC - abc_campi_product_template",

    'summary': """Modulo contente i campi aggiunti nelle anagrafiche prodotti.""",

    'description': """
       Modulo contente i campi aggiunti nelle anagrafiche prodotti.
    """,

    'author': "A.B.C. srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Product',
    'version': '0.1',

    'depends': ['base', "product", "stock"],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    "installable": True,
    "application": True,
    'demo': [],
}
