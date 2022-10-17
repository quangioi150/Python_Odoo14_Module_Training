# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Training',
    'version': '1.1',
    'category': 'Website/eLearning',
    'sequence': 95,
    'summary': 'Centralize training information',


    'website': 'https://www.odoo.com/page/training',
    'depends': [
        'website_slides', 'base', 'base_import'
    ],
    'data': [
        'views/training_view.xml',
        # 'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [
    ],
    'license': 'LGPL-3',
}
