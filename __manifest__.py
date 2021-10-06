# -*- coding: utf-8 -*-
{
    'name': "Vista_libros",  # Module title
    'summary': "Manage books easily10",  # Module subtitle phrase
    'description': """
Manage Library
==============
Description related to library.
    """,  # Supports reStructuredText(RST) format
    'author': "Parth Gajjar",
    'website': "http://www.example.com",
    'category': 'Tools',
    'version': '14.0.1',
    'depends': ['base'],
    'data': [
        'views/vista_tabla.xml',
        'views/vista_grafico.xml',
    ],

    # This demo data files will be loaded if db initialize with demo data (commented because file is not used in this example)
    # 'demo': [
    #     'data/demo.xml'
    # ],

    'instalable': True,
    'application': True
}
