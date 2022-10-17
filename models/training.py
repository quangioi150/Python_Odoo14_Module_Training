from odoo import fields, models


class Training(models.Model):
    _inherit = "slide.channel"

    sequence = fields.Integer(String="Number", default=1)
    date_updated = fields.Date(string='Date updated')
    course_name = fields.Char(String="Course Name")
    type = fields.Char(String="Type")
    privacy = fields.Char(String="Privacy")
    total_content = fields.Integer(string='Total content')
    total_learner = fields.Integer(string='Total learning')
    total_question = fields.Integer(string='Total question')
    status = fields.Selection([('action', 'Action'), ('draft', 'Draft'), ('inactive', 'Inactive')],
                              required=True)

