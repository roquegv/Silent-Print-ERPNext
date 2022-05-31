import frappe, base64
from frappe.utils.pdf import get_pdf,cleanup

@frappe.whitelist()
def create_pdf(doctype, name, silent_print_format, doc=None, no_letterhead=0):
	html = frappe.get_print(doctype, name, silent_print_format, doc=doc, no_letterhead=no_letterhead)
	options = get_pdf_options(silent_print_format)
	pdf = get_pdf(html, options=options)
	pdf_base64 = base64.b64encode(pdf)
	return pdf_base64.decode()

def get_pdf_options(silent_print_format):
	print_format = frappe.db.get_value("Silent Print Format", silent_print_format, "print_format")
	pf = frappe.get_doc("Print Format", print_format)
	options = {
		"page-size": pf.get("page_size") or "A4"
	}
	if pf.get("page_size") == "Custom":
		options = {
			"page-width": pf.get("custom_width"),
			"page-height": pf.get("custom_height")
		}
	return options