import requests
import os
import json

class Request(object):

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
