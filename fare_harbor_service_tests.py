from fareharbor.fare_harbor_service import FareHarborService
import unittest


class FareHarborServiceTest(unittest.TestCase):
    def setUp(self):
        self.service = FareHarborService()

    def test_gets_companies(self):
        self.assertEqual(self.service.get_companies(),
        {'companies': [{'shortname': 'bodyglove', 'name': 'Body Glove'}, {'shortname': 'islandsailing', 'name': 'Island Sailing'}, {'shortname': 'sharktourshawaii', 'name': 'North Shore Shark Adventures'}]})

    def test_gets_items(self):
        items = self.service.get_items('bodyglove')
        item_name = items['items'][0]['name']
        self.assertEqual(item_name, 'Snorkel & Dolphin Adventure')

    def test_gets_lodgings(self):
        lodgings = self.service.get_lodgings('bodyglove')
        lodging_name = lodgings['lodgings'][0]['name']
        self.assertEqual(lodging_name, 'Alii Cove')

    def test_gets_availabilites_by_date(self):
        availabilities = self.service.get_availabilities_by_date('sharktourshawaii', {'pk': 1108, 'date': '2016-11-14'})
        availability = availabilities['availabilities'][0]
        self.assertEqual(availability['capacity'], 18)

    def test_gets_availabilites_by_date_range(self):
        availabilities = self.service.get_availabilities_by_date_range('sharktourshawaii', {'pk': 1108, 'start_date': '2016-11-14', 'end_date': '2016-11-17'})
        availability = availabilities['availabilities'][0]
        self.assertEqual(availability['capacity'], 18)

    def test_gets_single_availability(self):
        availability = self.service.get_availability('bodyglove', 70050)['availability']
        self.assertEqual(availability['capacity'], 120)

    def test_gets_booking(self):
        booking = self.service.get_booking('bodyglove', '85ab9e4c-03fd-4bd4-af67-4946aa426c79')['booking']
        self.assertEqual(booking['uuid'], '85ab9e4c-03fd-4bd4-af67-4946aa426c79')
        self.assertIsNotNone(booking['status'])

    def test_gets_availability_lodgings(self):
        lodgings = self.service.get_availability_lodgings('bodyglove', 70050)
        lodging = lodgings['lodgings'][0]
        self.assertEqual(lodging['name'], 'Alii Cove')

    def test_posts_booking(self):
        booking = self.service.post_booking({'pk': 70043,
          'company_shortname': "bodyglove",
          'name': 'John Doe',
          'phone': '415-789-4563',
          'email': 'johndoe@example.com',
          'customer_type_rates': [149126, 149126],
          'note': 'Optional booking note',
          'voucher_number': 'VN-123456'})['booking']

        contact_info = booking['contact']
        self.assertEqual(booking['status'], 'booked')
        self.assertEqual(contact_info['phone'], '415-789-4563')
        self.assertEqual(contact_info['email'], 'johndoe@example.com')
        self.assertEqual(contact_info['name'], 'John Doe')

    def test_verifies_booking(self):
        verification = self.service.post_verify_booking({'pk': 70043,
          'company_shortname': 'bodyglove',
          'name': 'John Doe',
          'phone': '415-789-4563',
          'email': 'johndoe@example.com',
          'customer_type_rates': [149126, 149126],
          'note': 'Optional booking note',
          'voucher_number': 'VN-123456'})

        self.assertEqual(verification['is_bookable'], True)
        self.assertEqual(verification['invoice_price'], 28387)
        self.assertEqual(verification['receipt_total'], 28387)

    def test_deletes_booking(self):
        booking = self.service.post_booking({'pk': 70043,
          'company_shortname': "bodyglove",
          'name': 'John Doe',
          'phone': '415-789-4563',
          'email': 'johndoe@example.com',
          'customer_type_rates': [149126, 149126],
          'note': 'Optional booking note',
          'voucher_number': 'VN-123456'})['booking']

        cancelled_booking = self.service.delete_booking('bodyglove', booking['uuid'])['booking']

        self.assertEqual(cancelled_booking['uuid'], booking['uuid'])
        self.assertEqual(cancelled_booking['status'], 'cancelled')

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(FareHarborServiceTest))
    return test_suite

mySuite = suite()

runner = unittest.TextTestRunner()
runner.run(mySuite)
