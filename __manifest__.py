# -*- coding: utf-8 -*-
{
    'name': "km_data_overview",

    'summary': """
        """,

    'description': """
        
    """,

    'author': "Arash Homayounfar",
    'website': "https://gilaneh.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Service Desk/Service Desk',
    'application': True,
    'version': '1.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'mail', 'km_data'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/diagram.xml',
        'views/views.xml',
        'views/location.xml',
    ],
    'assets': {
        # 'website.assets_editor': [
        #     'static/src/**/*',
        # ],

        'web.assets_frontend': [
            'km_data_overview/static/src/css/style.scss',
            'km_data_overview/static/src/js/diagram_frontend.js'
        ],
        'web.assets_backend': [
            'km_data_overview/static/src/css/style.scss',
            # 'km_data_overview/static/src/css/styles.css',
            'km_data_overview/static/src/lib/interactjs/interact.min.js',
            'km_data_overview/static/src/js/diagram_process.js',
        ],
        'web.report_assets_common': [
            'km_data_overview/static/src/css/report_styles.css',
            # 'km_data_overview/static/src/js/website_form_km_data_overview.js'
        ],

    },

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',

}
