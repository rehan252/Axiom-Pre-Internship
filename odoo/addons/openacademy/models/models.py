from odoo import models, fields, api, exceptions, _
from datetime import timedelta


class Course(models.Model):
    _name = "openacademy.course"

    name = fields.Char(string='Title', required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.users', ondelete='set null', string='Responsible', index=True)
    session_ids = fields.One2many('openacademy.session', 'course_id', string='Sessions')

    # As title is unique so, we add Copy text with Title
    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copies_count = self.search_count(
            [('name', '=like', _(u"Copy of {}%").format(self.name))]
        )
        if not copies_count:
            new_name = _(u"Copy of {}").format(self.name)
        else:
            new_name = _(u"Copy of {} {}").format(self.name, copies_count)

        default['name'] = new_name
        return super(Course, self).copy(default)

    # sql constraints conditions to make title and unique and different from description
    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title and description of course should not be same"),

        ('name_unique',
         'UNIQUE(name)', "The course title must be unique")
    ]


class Session(models.Model):
    _name = "openacademy.session"

    name = fields.Char(required=True)
    start_date = fields.Date(default=fields.Date.today)
    duration = fields.Float(digits=(6, 2), help="Duration in days")  # (6,2) defines precision of Float
    seats = fields.Integer(string="Number of seats")
    active = fields.Boolean(default=True)
    color = fields.Integer()

    instructor_id = fields.Many2one('res.partner', string='Instructor', ondelete='cascade',
                                    domain=['|', ('instructor', '=', True), ('category_id.name', 'ilike', 'Teacher')])
    course_id = fields.Many2one('openacademy.course', string='Course', ondelete='cascade', required=True)
    attendee_ids = fields.Many2many('res.partner', string='Attendees')

    taken_seats = fields.Float(string='Seats Taken', compute='_taken_seats')
    end_date = fields.Date(string='End Date', store=True, compute='_get_end_date', inverse='_set_end_date')
    attendees_count = fields.Integer(string="Number of Attendees", compute='_get_attendees_count', store=True)

    # To calculate the taken seats and available
    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for s in self:
            if not s.seats:
                s.taken_seats = 0.0
            else:
                s.taken_seats = 100.0 * len(s.attendee_ids) / s.seats

    # When seats value change re-calculate remaining and taken seats
    @api.onchange('seats', 'attendee_ids')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': _("Incorrect 'seats' value"),
                    'message': _("The number of available seats may not be negative")
                }
            }
        if self.seats < len(self.attendee_ids):
            return {
                'warning': {
                    'title': _("Too many attendees"),
                    'message': _("Increase seats or remove excess attendees")
                }
            }

# get the end date of course based on starting date and duration
    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for s in self:
            if not (s.start_date and s.end_date):
                s.end_date = s.start_date
                continue

            start = fields.Datetime.from_string(s.start_date)
            duration = timedelta(days=s.duration, seconds=-1)
            s.end_date = start + duration

    @api.depends('duration')
    def _set_end_date(self):
        for s in self:
            if not (s.start_date and s.end_date):
                continue

            start_date = fields.Datetime.from_string(s.start_date)
            end_date = fields.Datetime.from_string(s.end_date)
            duration = (end_date - start_date).days + 1

    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for s in self:
            s.attendees_count = len(s.attendee_ids)

    # Validate constraints of Model
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendee(self):
        for s in self:
            if s.instructor_id and s.instructor_id in s.attendee_ids:
                raise exceptions.ValidationError(_("A session's instructor can't be attendee"))




