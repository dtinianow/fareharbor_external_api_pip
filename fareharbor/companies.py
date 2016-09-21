from fare_harbor_service import FareHarborService
from company import Company

class Companies(object):

    def all(self):
        raw_data = FareHarborService().get_companies()
        company_data = raw_data['companies']
        companies = [ Company(i) for i in companies_data ]
        return companies


    def find(self, shortname):
        companies = self.all()
        return next(company for company in companies if company.shortname == shortname)
