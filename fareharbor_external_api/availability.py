class Availability(object):
    def __init__(self, params):
        for key in params:
            setattr(self, key, params[key])

a = {'capacity': 10, 'customer_type_rates': [1, 5], 'custom_field_instances': "", 'item': 'nope', 'pk': 6, 'start_at': 'mmm never', 'end_at': 'mmm yesterday'}

avail = Availability(a)

print avail
print avail.capacity
print avail.customer_type_rates
print avail.custom_field_instances
print avail.item
print avail.start_at
print avail.end_at
