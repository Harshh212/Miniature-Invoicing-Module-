import frappe

def calculate_total(doc, method):
    """
    Calculates the total amount for an invoice and updates the grand_total.
    This function is triggered by the 'validate' hook before the document is saved.
    """
    # Initialize grand_total to 0 before recalculating
    doc.grand_total = 0.0

    # Iterate through all the line items in the invoice_items child table
    for item in doc.invoice_items:
        # Calculate the amount for the current line item (quantity * rate)
        item.amount = item.quantity * item.rate
        
        # Add the line item's amount to the overall grand total
        doc.grand_total += item.amount
