from odoo import models, fields


class AccountPaymentRecibo(models.Model):
    _inherit = "account.payment"
    x_numero_recibo = fields.Char(string="Recibo de Dinero N°", copy=False, default='New', readonly=True)


    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('payment.recibo_seq') or 'New'

        result= super(AccountPaymentRecibo, self).create(vals)

        return result


