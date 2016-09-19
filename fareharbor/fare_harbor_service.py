import requests
import os
import json

class FareHarborService:

    # url = 'https://demo.fareharbor.com/api/external/v1/'
    # api_app_key = os.environ['FAREHARBOR_API_APP_KEY']
    # api_user_key = os.environ['FAREHARBOR_API_USER_KEY']
    # payload = {'api-app': api_app_key, 'api-user': api_user_key}

    def __init__(self):
        self.url = 'https://demo.fareharbor.com/api/external/v1/'
        self.api_app_key = os.environ['FAREHARBOR_API_APP_KEY']
        self.api_user_key = os.environ['FAREHARBOR_API_USER_KEY']
        self.payload = {'api-app': self.api_app_key, 'api-user': self.api_user_key}

    def get_companies(self):
        response = requests.get('%scompanies/' % self.url, params=self.payload)
        return response.json()

    def get_items(self, shortname):
        response = requests.get('%scompanies/%s/items/' % (self.url, shortname), params=self.payload)
        return response.json()

    def get_availabilities_by_date(self, shortname, data):
        response = requests.get('%scompanies/%s/items/%s/minimal/availabilities/date/%s/' % (self.url, shortname, data['pk'], data['date']), params=self.payload)
        return response.json()

    def get_availabilities_by_date_range(self, shortname, data):
        response = requests.get('%scompanies/%s/items/%s/minimal/availabilities/date-range/%s/%s/' % (self.url, shortname, data['pk'], data['start_date'], data['end_date']), params=self.payload)
        return response.json()

    def get_availability(self, shortname, pk):
        response = requests.get('%scompanies/%s/availabilities/%s/' % (self.url, shortname, pk), params=self.payload)
        return response.json()

    def get_booking(self, shortname, uuid):
        response = requests.get('%scompanies/%s/bookings/%s/' % (self.url, shortname, uuid), params=self.payload)
        return response.json()

    def get_lodgings(self, shortname):
        response = requests.get('%scompanies/%s/lodgings/' % (self.url, shortname), params=self.payload)
        return response.json()

    def get_availability_lodgings(self, shortname, pk):
        response = requests.get('%scompanies/%s/availabilities/%s/lodgings/' % (self.url, shortname, pk), params=self.payload)
        return response.json()

    def post_booking(self, data):
        raw_booking = self.format_booking_body(data)
        booking = json.dumps(raw_booking)
        response = requests.post('%scompanies/%s/availabilities/%s/bookings/' % (self.url, data['company_shortname'], data['pk']), data=booking, params=self.payload)
        return response.json()

    def post_verify_booking(self, data):
        raw_booking = self.format_booking_body(data)
        booking = json.dumps(raw_booking)
        response = requests.post('%scompanies/%s/availabilities/%s/bookings/validate/' % (self.url, data['company_shortname'], data['pk']), data=booking, params=self.payload)
        return response.json()

    def delete_booking(self, shortname, uuid):
        response = requests.delete('%scompanies/%s/bookings/%s/' % (self.url, shortname, uuid), params=self.payload)
        return response.json()

    def format_booking_body(self, data):
        return {
          'voucher_number': data['voucher_number'],
          'contact': {
            'name': data['name'],
            'phone': data['phone'],
            'email': data['email']
          },
          'customers': self.customer_types(data['customer_type_rates']),
          'note': 'Optional booking note'
        }

    def customer_types(self, types):
        for i in range(len(types)):
            types[i] = {'customer_type_rate': types[i]}
        return types


#### The code below can be used for testing each method:

# x = FareHarborService()
#
# x.get_companies()
# x.get_items('bodyglove')
# data_1 = {'pk': 1108, 'date': '2016-11-14'}
# x.get_availabilities_by_date('sharktourshawaii', data_1)
# data_2 = {'pk': 1108, 'start_date': '2016-11-14', 'end_date': '2016-11-17'}
# x.get_availabilities_by_date_range('sharktourshawaii', data_2)
# x.get_availability('bodyglove', 70050)
# x.get_booking('bodyglove', '85ab9e4c-03fd-4bd4-af67-4946aa426c79')
# x.get_lodgings('bodyglove')
# x.get_availability_lodgings('bodyglove', 70050)
# booking = {
#         'pk': 70043,
#         'company_shortname': 'bodyglove',
#         'name': 'John Doe',
#         'phone': '415-789-4563',
#         'email': 'johndoe@example.com',
#         'customer_type_rates': [149126, 149126],
#         'note': 'Optional booking note',
#         'voucher_number': 'VN-123456'
# }
# x.post_booking(booking)
# x.post_verify_booking(booking)
# x.delete_booking('bodyglove', '6e62d9e8-163b-446b-83d5-2e3f344100ae')

# import code; code.interact(local=dict(globals(), **locals()))
