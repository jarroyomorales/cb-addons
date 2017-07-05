# -*- coding: utf-8 -*-
# Copyright 2016-2017 LasLabs Inc.
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Creu Blanca Demo Database',
    'summary': '',
    'version': '10.0.1.0.0',
    'author': 'Eficent, Odoo Community Association (OCA)',
    'category': '',
    'depends': [
        'workflow_plandefinition',
        'product',
        'medical',
        'medical_center',
        'medical_encounter',
        'base',
        'stock',
        'medical_insurance',
        'medical_insurance_sale',
        'medical_encounter_careplan',
        'medical_careplan',
        'medical_request_group',
        'medical_practitioner',
        'medical_procedure',
    ],
    'demo': [
        'demo/workflow_types_demo.xml',
        'demo/products_demo.xml',
        'demo/activity_definitions_demo.xml',
        'demo/plan_definition_demo.xml',
        'demo/center_demo.xml',
        'demo/encounter_demo.xml',
        'demo/insurance_demo.xml',
        'demo/careplan_demo.xml',
        'demo/request_group_demo.xml',
        'demo/practitioner_demo.xml',
        'demo/procedure_request_demo.xml',
    ],
    'website': '',
    'licence': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
