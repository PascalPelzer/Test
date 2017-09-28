# -*- coding: utf-8 -*-
# Copyright 2016 ACSONE SA/NV (<http://acsone.eu>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': "Test",
    'description': """
        Odoo aplication for Test""",
    'author': 'MATRUM SA',
    'website': "http://metrum.lu",
    'category': 'Test',
    'version': '10.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        # Test open source addons
        # !!! no odoo enterprise addons dependencies !!!
        # OCA/server-tools
        'contacts',
    ],
    'data': [
    ],
    'application': True,
}
