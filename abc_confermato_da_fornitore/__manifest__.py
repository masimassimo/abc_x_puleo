# -*- coding: utf-8 -*-
{
    'name': "ABC - abc_confermato_da_fornitore",

    'summary': """ Se il campo dell'ordine di acquisto non viene modificato dopo 3 giorni crea il ToDo.""",

    'description': """ Se il campo dell'ordine di acquisto non viene modificato dopo 3 giorni crea il ToDo. """,

    'author': "A.B.C. Srl",
    'website': "https://www.abcstrategie.it/",

    'category': 'Purchase',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data/scheduled_action.xml'
    ],
    "installable": True,
    "application": True,
    # only loaded in demonstration mode
    'demo': [],
}
