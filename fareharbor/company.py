from fare_harbor_service import FareHarborService
from item import Item

class Company:

    def __init__(self, company):
        self.name = company['name']
        self.shortname = company['shortname']


    # def items(self):
    #     items = FareHarborService().get_items(self.shortname)
    #     for i in items:
    #         Item(i)
    #
    # def availabilities_by_date(data):
    #     availabilities = FareHarborService

    # def availabilities_by_date_range(data):
    #
    #
    # def availability(pk):
    #
    #
    # def booking(uuid):
    #
    #
    # def lodgings():
    #
    #
    # def availability_lodgings(pk):
    #
    #
    # def create_booking(booking_request):
    #
    #
    # def verify_booking(booking_data):
    #
    #
    # def cancel_booking(uuid):

# a = Company({'name': 'Body Glove', 'shortname': 'bodyglove'}).items()
