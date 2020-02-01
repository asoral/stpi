# -*- coding: utf-8 -*-
{
	'name': 'Tour Request',
	'version': '12.0.1.0.0',
	'summary': 'Tour Request',
	'category': 'Tools',
	'author': 'Dexciss Technologies Pvt Ltd(@ RGupta)',
	'maintainer': 'dexciss Techno Solutions',
	'company': 'dexciss Techno Solutions',
	'website': 'https://www.dexciss.com',
	'depends': ['base','hr'],
	'data': [
		'security/ir.model.access.csv',
		'security/security.xml',
		'data/travel_mode_demo_data.xml',
        'views/tour_request.xml',
	],
	'images': [],
	'license': 'AGPL-3',
	'installable': True,
	'application': False,
	'auto_install': False,
}