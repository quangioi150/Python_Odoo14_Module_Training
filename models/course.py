from odoo import fields, models

class Traning(models.Model):
    _name = "course"
    course_name = fields.Char(string='Course Name')
    course_description = fields.Char(string='Course Description')
    category = fields.Many2many('category', string='Category')
    type = fields.Char(string='Type')
    privacy = fields.Char(string='Privacy')
    status = fields.Char(string='Status')

