app_name = "flows"
app_title = "Flows"
app_publisher = "Arun Logistics"
app_description = "Implements custom workflows for Arun Logistics"
app_icon = "icon-book"
app_color = "#589494"
app_email = "bhupesh00gupta@gmail.com"
app_url = "No URL yet"
app_version = "0.0.1"

fixtures = [
    "Custom Field",
    "Supplier Type",
    "Item Group",
    "Warehouse",
    "Item",
    "Item Conversion"
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/flows/css/flows.css"
# app_include_js = "/assets/flows/js/flows.js"

# include js, css files in header of web template
# web_include_css = "/assets/flows/css/flows.css"
# web_include_js = "/assets/flows/js/flows.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "flows.install.before_install"
# after_install = "flows.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "flows.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"flows.tasks.all"
# 	],
# 	"daily": [
# 		"flows.tasks.daily"
# 	],
# 	"hourly": [
# 		"flows.tasks.hourly"
# 	],
# 	"weekly": [
# 		"flows.tasks.weekly"
# 	]
# 	"monthly": [
# 		"flows.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "flows.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.core.doctype.event.event.get_events": "flows.event.get_events"
# }


boot_session = "flows.flows.startup_boot_info.boot_session"



jenv_filter = [
    'indent_refill_qty:flows.jinja_filters.indent_refill_qty',
    'indent_oneway_qty:flows.jinja_filters.indent_oneway_qty',
    'compute_erv_for_refill_in_indent:flows.jinja_filters.compute_erv_for_refill_in_indent',
    'get_contract_number:flows.jinja_filters.get_contract_number',
    'get_registration_code:flows.jinja_filters.get_registration_code',
    'get_customer_tin_number:flows.jinja_filters.get_customer_tin_number',
    'get_cenvat_status:flows.jinja_filters.get_cenvat_status',
]