from odoo import api, fields, models, tools, _
import calendar
import datetime
from dateutil.relativedelta import relativedelta

class HREmployee(models.Model):
    _inherit = "hr.employee"
    _description = "Employee Directory"

    is_previous_month = fields.Boolean('Hello')
