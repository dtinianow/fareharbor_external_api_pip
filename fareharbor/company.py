from fare_harbor_service import FareHarborService
from item import Item
from availability import Availability
from booking import Booking
from lodging import Lodging
from verification import Verification

class Company:

    def __init__(self, company):
        self.name = company['name']
        self.shortname = company['shortname']

    def items(self):
        raw_items = FareHarborService().get_items(self.shortname)
        items_data = raw_items['items']
        items = []
        for i in items_data:
            items.append(Item(i))
        return items

    def availabilities_by_date(self, data):
        raw_availabilities = FareHarborService().get_availabilities_by_date(self.shortname, data)
        availabilities_data = raw_availabilities['availabilities']
        availabilities = []
        for i in availabilities_data:
            availabilities.append(Availability(i))
        return availabilities

    def availabilities_by_date_range(self, data):
        raw_availabilities = FareHarborService().get_availabilities_by_date_range(self.shortname, data)
        availabilities_data = raw_availabilities['availabilities']
        availabilities = []
        for i in availabilities_data:
            availabilities.append(Availability(i))
        return availabilities

    def availability(self, pk):
        raw_availability = FareHarborService().get_availability(self.shortname, pk)
        availability_data = raw_availability['availability']
        return Availability(availability_data)

    def booking(self, uuid):
        raw_booking = FareHarborService().get_booking(self.shortname, uuid)
        booking_data = raw_booking['booking']
        return Booking(booking_data)

    def lodgings(self):
        raw_lodgings = FareHarborService().get_lodgings(self.shortname)
        lodgings_data = raw_lodgings['lodgings']
        lodgings = []
        for i in lodgings_data:
            lodgings.append(Lodging(i))
        return lodgings

    def availability_lodgings(self, pk):
        raw_lodgings = FareHarborService().get_availability_lodgings(self.shortname, pk)
        lodgings_data = raw_lodgings['lodgings']
        lodgings = []
        for i in lodgings_data:
            lodgings.append(Lodging(i))
        return lodgings

    def create_booking(self, booking_request):
        raw_booking = FareHarborService().post_booking(booking_request)
        booking_data = raw_booking['booking']
        return Booking(booking_data)

    def verify_booking(self, booking_data):
        booking = FareHarborService().post_verify_booking(booking_data)
        return Verification(booking)

    def cancel_booking(self, uuid):
        raw_cancelled_booking = FareHarborService().delete_booking(self.shortname, uuid)
        cancelled_booking = raw_cancelled_booking['booking']
        return Booking(cancelled_booking)

# a = Company({'name': 'Body Glove', 'shortname': 'bodyglove'}).items()
# b = Company({'name': 'North Shore Shark Adventures', 'shortname': 'sharktourshawaii'}).availabilities_by_date({'pk': 1108, 'date': '2016-11-14'})
# c = Company({'name': 'North Shore Shark Adventures', 'shortname': 'sharktourshawaii'}).availabilities_by_date_range({'pk': 1108, 'start_date': '2016-11-14', 'end_date': '2016-11-17'})
# d = Company({'name': 'Body Glove', 'shortname': 'bodyglove'}).availability(70050)
# e = Company({'name': 'Body Glove', 'shortname': 'bodyglove'}).booking('85ab9e4c-03fd-4bd4-af67-4946aa426c79')
# f = Company({'name': 'Body Glove', 'shortname': 'bodyglove'}).lodgings()
# g = Company({'name': 'Body Glove', 'shortname': 'bodyglove'}).availability_lodgings(70050)
# h = Company({'name': 'Body Glove', 'shortname': 'bodyglove'}).create_booking({'pk': 70050,
#         'company_shortname': 'bodyglove',
#         'name': 'John Doe',
#         'phone': '415-789-4563',
#         'email': 'johndoe@example.com',
#         'customer_type_rates': [149140],
#         'note': 'Optional booking note',
#         'voucher_number': 'VN-123456'})
# i = Company({'name': 'Body Glove', 'shortname': 'bodyglove'}).verify_booking({'pk': 70050,
#         'company_shortname': 'bodyglove',
#         'name': 'John Doe',
#         'phone': '415-789-4563',
#         'email': 'johndoe@example.com',
#         'customer_type_rates': [149140],
#         'note': 'Optional booking note',
#         'voucher_number': 'VN-123456'})
# j = Company({'name': 'Body Glove', 'shortname': 'bodyglove'}).cancel_booking(h.uuid)
#
# print a[0].name
# print b[0].start_at
# print c[0].capacity
# print d.item
# print e.status
# print f[0].name
# print g[-1].name
# print h.status
# print h.uuid
# print i.status
# print j.status
