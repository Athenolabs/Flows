# Copyright (c) 2013, Arun Logistics and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe


def execute(filters=None):
	missing_map, books_map, max_missing = get_missing_map(filters)
	columns = get_columns(max_missing)

	data = []
	for missing_book in sorted(missing_map.keys()):
		book_ref = books_map[missing_book]
		missing_list = missing_map[missing_book]
		row = [
			book_ref.name,
			book_ref.warehouse,
			book_ref.pr_debit,
			book_ref.issued_to
		]
		row.extend(missing_list)
		data.append(row)

	data = sorted(data, key=lambda x: (x[1], x[2]))

	return columns, data


def get_missing_map(filters=None):
	books = frappe.db.sql(
		"""
		SELECT name, warehouse, issued_to, pr_debit,
		serial_start, serial_end
		FROM `tabGoods Receipt Book` WHERE
		name NOT IN ("GBR#0-500") AND state != 'Closed/Received';
		""", as_dict=True)

	books_map = {}
	missing_map = {}

	max_missing = 0
	for book in books:
		books_map[book.name] = book

		data = frappe.db.sql("""
		SELECT goods_receipt_number FROM `tabGoods Receipt` WHERE docstatus = 1
		AND goods_receipt_number BETWEEN {} AND {};
		""".format(book.serial_start, book.serial_end))
		gr_list = [int(x[0]) for x in data if x[0].isnumeric()]

		data = frappe.db.sql("""
		SELECT id FROM `tabPayment Receipt` WHERE docstatus = 1
		AND id BETWEEN {} AND {};
		""".format(book.serial_start, book.serial_end))

		pr_list = [int(x[0]) for x in data if x[0].isnumeric()]

		data_list = gr_list + pr_list

		if not data_list:
			continue

		missing = sorted(set(xrange(min(data_list), max(data_list))) - set(data_list))

		if missing:
			missing_map[book.name] = missing
			if len(missing) > max_missing:
				max_missing = len(missing)

	return missing_map, books_map, max_missing


def get_columns(max_missing):
	d = [
		"Book Id:Link/Goods Receipt Book:170",
		"Warehouse:Warehouse:150",
		"PR Debit A/c",
		"Issued To::100",
	]
	if max_missing > 0:
		d.extend(["Missing {}".format(i + 1) for i in xrange(0, max_missing)])

	return d