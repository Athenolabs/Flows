# Copyright (c) 2013, Arun Logistics and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class EndOfDay(Document):
	def validate(self):
		old_gr_eod = frappe.db.get_single_value("End Of Day", "gr_eod")

		if self.gr_eod < old_gr_eod:
			if frappe.session.user == "Administrator":
				frappe.msgprint("Day/Days Unlocked")
			else:
				frappe.throw("Can Not Unlock Days")
