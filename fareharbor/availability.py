class Availability:
    def __init__(self, availability):
            self.capacity               = availability['capacity']
            self.customer_type_rates    = availability['customer_type_rates']
            self.custom_field_instances = availability['custom_field_instances']
            self.item                   = availability['item']
            self.pk                     = availability['pk']
            self.start_at               = availability['start_at']
            self.end_at                 = availability['end_at']
