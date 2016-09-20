class Verification:
    
    def __init__(self, verification):
        self.invoice_price    = verification['invoice_price']
        self.receipt_taxes    = verification['receipt_taxes']
        self.receipt_subtotal = verification['receipt_subtotal']
        self.pickup           = verification['pickup']
        self.receipt_total    = verification['receipt_total']
        self.is_bookable      = verification['is_bookable']
