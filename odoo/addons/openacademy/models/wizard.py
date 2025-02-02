from odoo import models, fields, api


class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'

    def _default_session(self):
        return self.env['openacademy.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2one('openacadmey.session', string="Sessions", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees", default="_default_session")

    @api.multi
    def subscribe(self):
        for session in session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}
