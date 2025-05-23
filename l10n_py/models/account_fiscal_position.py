# -*- coding: utf-8 -*-
from odoo import fields, models, api, _


class AccountFiscalPosition(models.Model):

    _inherit = 'account.fiscal.position'

    l10n_py_set_responsibility_type_ids = fields.Many2many(
        'l10n_py.set.responsibility.type', 'l10n_py_set_reponsibility_type_fiscal_pos_rel',
        string='SET Responsibility Types', help='List of SET responsibilities where this fiscal position '
        'should be auto-detected')

    def _get_fpos_ranking_functions(self, partner):
        if self.env.company.country_id.code != "PY":
            return super()._get_fpos_ranking_functions(partner)
        return [
            ('l10n_py_set_responsibility_type_id', lambda fpos: (
                partner.l10n_py_set_responsibility_type_id in fpos.l10n_py_set_responsibility_type_ids
            ))
        ] + super()._get_fpos_ranking_functions(partner)
