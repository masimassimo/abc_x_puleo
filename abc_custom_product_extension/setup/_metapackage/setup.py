import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-product-extension",
    description="Meta package for product-extension Odoo addons",
    version=version,
    install_requires=[
        #'odoo14-addon-account_financial_report',
        #'odoo14-addon-account_tax_balance',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)