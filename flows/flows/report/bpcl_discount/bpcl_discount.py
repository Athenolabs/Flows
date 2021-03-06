# Copyright (c) 2013, Arun Logistics and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt
from flows.stdlogger import root



def execute(filters=None):
	return get_columns(filters), get_data(filters)


def get_columns(filters):
	return [
		"DATE:Date:",
		"CUSTOMER:Link/Customer:250",
		"INVOICE NO.:Data:",
		"CC NO:Int:",
		"Package:Data:",
		"CYL:Int:",
		"QTY:Int:",
		"DISC:Currency:",
		"AMT:Currency:",
		"PROPOSAL ID:Data:",
		"II:Link/Indent Invoice:",
		"Field Officer:Data:100"
	]


def get_data(filters):
	invoices = get_invoices(filters)
	rows = []

	for invoice in invoices:
		policy_name, proposal_id = frappe.db.get_value(
			"Customer Plant Variables", invoice.customer_plant_variables, ["omc_policy", "contract_number"]
		)
		policy = get_policy(policy_name)
		rs = policy.execute(invoice.name)

		if rs['discount_mismatch'] == 0:
			continue

		c_factor = get_conversion_factor_item(invoice.item)

		rows.append([
			invoice.transaction_date,
			invoice.customer,
			invoice.invoice_number,
			invoice.customer_code,
			c_factor,
			invoice.qty,
			c_factor * invoice.qty,
			rs['discount_mismatch'],
			c_factor * invoice.qty * rs['discount_mismatch'],
			proposal_id if proposal_id else "Insert Discount Proposal",
			invoice.name,
			invoice.field_officer
		])

	return rows


def get_invoices(filters):

	cond = ' and r.field_officer = "{}"'.format(filters.field_officer) \
	if filters.field_officer else ''

	return frappe.db.sql("""
	Select i.*, r.customer_code, r.field_officer from `tabIndent Invoice` i
	left join `tabOMC Customer Registration` r
	on i.omc_customer_registration = r.name
	where i.docstatus = 1
	and i.supplier like 'bpcl%'
	and i.item != 'FCBK'
	and i.transaction_date between "{from_date}" and "{to_date}"
	{cond}
	and discount != 0
	order by i.customer, i.transaction_date asc
	""".format(cond=cond, **filters), as_dict=True)


def get_conversion_factor_item(item):
	return flt(item.replace('FC', '').replace('L', '').replace('EC', ''))


policies = {}
def get_policy(policy):
	if policy not in policies:
		p_obj = frappe.get_doc("OMC Policies", policy)
		p_obj.init()
		policies[policy] = p_obj
	return policies[policy]