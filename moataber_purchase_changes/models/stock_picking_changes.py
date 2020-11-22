# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import Warning
# Ahmed Salama Code Start ---->


class StockPickingInherit(models.Model):
	_inherit = 'stock.picking'
	
	driver_name = fields.Char("Driver Name")
	car_number = fields.Char("Car Number")
	port_weight = fields.Char("Port Balance Weight")
	transfer_comp_name = fields.Char("Transfer Company Name")

# Ahmed Salama Code End.
