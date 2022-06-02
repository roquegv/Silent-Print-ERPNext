# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "silent_print"
app_title = "Silent Print"
app_publisher = "Roque Vera"
app_description = "Silent print using https://github.com/imTigger/webapp-hardware-bridge"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "roquegv@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/silent_print/css/silent_print.css"
# app_include_js = "/assets/silent_print/js/silent_print.js"

# include js, css files in header of web template
# web_include_css = "/assets/silent_print/css/silent_print.css"
# web_include_js = "/assets/silent_print/js/silent_print.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "silent_print.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "silent_print.install.before_install"
# after_install = "silent_print.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "silent_print.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
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
# 		"silent_print.tasks.all"
# 	],
# 	"daily": [
# 		"silent_print.tasks.daily"
# 	],
# 	"hourly": [
# 		"silent_print.tasks.hourly"
# 	],
# 	"weekly": [
# 		"silent_print.tasks.weekly"
# 	]
# 	"monthly": [
# 		"silent_print.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "silent_print.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "silent_print.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "silent_print.task.get_dashboard_data"
# }

# injected in desk.html
app_include_js = "assets/js/silent_print.min.js"
# app_include_css = "assets/js/app.min.css"

page_js = {"point-of-sale" : "public/js/silent_print.js"}