# -*- coding: utf-8 -*-
# © 2011 Raphaël Valyi, Renato Lima, Guewen Baconnier, Sodexis
# © 2017 Mourad EL HADJ MIMOUNE, Akretion
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class HrPayslipConfirm(models.TransientModel):
    _name = 'hr.payslip.run.confirm'
    _inherit = ['exception.rule.confirm']

    related_model_id = fields.Many2one('hr.payslip.run', 'Hr Payslip Batch')

    @api.multi
    def action_confirm(self):
        self.ensure_one()
        if self.ignore:
            self.related_model_id.ignore_exception = True
        return super(HrPayslipConfirm, self).action_confirm()
