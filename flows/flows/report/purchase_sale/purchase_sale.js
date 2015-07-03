// Copyright (c) 2013, Arun Logistics and contributors
// For license information, please see license.txt

frappe.query_reports["Purchase Sale"] = {
	"filters":[
		{
			"fieldname":"from_date",
			"label":__("From Date"),
			"fieldtype":"Date",
			"default":frappe.datetime.month_start(),
			"reqd":1
		},
		{
			"fieldname":"to_date",
			"label":__("To Date"),
			"fieldtype":"Date",
			"default":frappe.datetime.month_end(),
			"reqd":1
		},
		{
			"fieldname":"lot_vot_bifurcate",
			"label":__("LOT VOT Bifurcate"),
			"fieldtype":"Check",
			"default":0
		},
		{
			"fieldname":"show_material_returned",
			"label":__("Show Material Returned"),
			"fieldtype":"Check",
			"default":0
		}

	]
};