# Copyright 2020-22 Manish Kumar Bohra <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

{
    'name': 'Bulk Lock Sales Orders',
    'version': '1.0.0',
    'summary': 'This app allows you to lock multiple sales order in bulk',
    'description': 'This app allows you to lock multiple sales order in bulk',
    'category': 'Sales',
    'author': 'Manish Bohra',
    'website': 'www.linkedin.com/in/manishkumarbohra',
    'maintainer': 'Manish Bohra',
    'support': 'manishkumarbohra@outlook.com',
    'sequence': '10',
    'license': 'LGPL-3',
    "data": [
        'views/bulk_sales.xml',
    ],
    'images': ['static/description/banner.png'],
    'depends': ['sale', 'sale_management'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
