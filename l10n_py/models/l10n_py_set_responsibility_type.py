# -*- coding: utf-8 -*-

from odoo import models, fields


class L10nArAfipResponsibilityType(models.Model):

    _name = 'l10n_py.set.responsibility.type'
    _description = 'SET Responsibility Type'
    _order = 'sequence'

    name = fields.Char(required=True, index='trigram')
    sequence = fields.Integer()
    code = fields.Char(required=True, index=True)
    active = fields.Boolean(default=True)

    _sql_constraints = [('name', 'unique(name)', 'Name must be unique!'),
                        ('code', 'unique(code)', 'Code must be unique!')]
