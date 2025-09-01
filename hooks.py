app_name = "invoicing"
app_title = "Invoicing Module"
app_publisher = "None"
app_description = "None"
app_email = "chaudhariharsh212@gmail.com"
app_license = "mit"

# Document Events
# ---------------
# Hook on document methods and events
doc_events = {
    "Invoice": {
        "validate": "invoicing.invoice.calculate_total"
    }
}
