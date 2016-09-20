from fare_harbor_service import FareHarborService
from company import Company

class Companies:

    def all(self):
        raw_data = FareHarborService().get_companies()
        company_data = raw_data['companies']
        companies = []
        for i in company_data:
            companies.append(Company(i))
        return companies

    def find(self, shortname):
        companies = self.all()
        return next(company for company in companies if company.shortname == shortname)
