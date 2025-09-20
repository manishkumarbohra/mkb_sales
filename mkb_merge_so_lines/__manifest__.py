# Copyright 2020-22 Manish Kumar Bohra <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

{
    'name': 'Merge Duplicate Sale Order Line',
    'version': '1.0.0',
    'summary': 'This app allows you to Merge duplicate so lines',
    'description': 'This app allows you to Merge duplicate so lines',
    'category': 'Sales',
    'author': 'Manish Bohra',
    'website': 'www.linkedin.com/in/manishkumarbohra',
    'maintainer': 'Manish Bohra',
    'support': 'manishkumarbohra@outlook.com',
    'sequence': '10',
    'license': 'LGPL-3',
    "data": [
        'views/merge_so_line.xml',
    ],
    'images': ['static/description/banner.png'],
    'depends': ['sale', 'sale_management'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
