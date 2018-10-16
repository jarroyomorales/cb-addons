# Copyright 2018 Creu Blanca
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Flag Box",
    "version": "11.0.1.0.0",
    "author": "Creu Blanca, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "category": "Website",
    "summary": "Allows to us a flag box with icons / buttons",
    "depends": [
        "web",
    ],
    "data": [
        "views/templates.xml",
    ],
    "qweb": ["static/src/xml/*.xml"],
    "installable": True,
}