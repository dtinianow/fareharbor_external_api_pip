from fare_harbor_service import FareHarborService
import json

class Companies(FareHarborService):

    def all(self):
        raw_data = FareHarborService().get_companies()
        return raw_data['companies']
        # companies = raw_data['companies']
        # for i in companies:
        #     print companies[i]

x = Companies()
x.all()

# class Companies(FareHarborService):
#
#     def service(self):
#         print FareHarborService().get_companies()
#
# x = Companies()
# x.service()
