# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Import Purchase Order Lines from Excel or CSV File',
    'version': '10.0.0.0',
    'summary': 'Easy to Import multiple Purchase order lines on Odoo by Using CSV/XLS file',
    'description': """
	BrowseInfo developed a new odoo/OpenERP module apps.
	This module use for import bulk purchase Order lines from Excel file. Import purchase order lines from CSV or Excel file.
	Import purchases, Import purchase order line, Import purchase lines, Import PO Line. purchase Import, Add PO from Excel.Add Excel Purchase order lines.Add CSV file.Import Purchase data. Import excel file
	-
    """,
    'author': 'BrowseInfo',
    "price": 20,
    "currency": 'EUR',
    'website': 'http://www.browseinfo.in',
    
    'depends': ['base','purchase'],
    'data': [
    		  'import_po_lines_view.xml',
            ],
    'demo': [],
    'test': [],
    'installable':True,
    'auto_install':False,
    'application':True,
    "images":['static/description/Banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
