class Availability(object):
    def __init__(self, params):
        for key in params:
            setattr(self, key, params[key])

a = {'capacity': 10, 'customer_type_rates': [1, 5], 'custom_field_instances': "", 'item': 'nope', 'pk': 6, 'start_at': 'mmm never', 'end_at': 'mmm yesterday'}

avail = Availability(a)
