from fare_harbor_service import FareHarborService
from company import Company

class Companies(object):

    @classmethod
    def all(cls):
        raw_data = FareHarborService().get_companies()
        company_data = raw_data['companies']
        return [ Company(i) for i in company_data ]

    @classmethod
    def find(cls, shortname):
        companies = cls.all()
        print next(company for company in companies if company.shortname == shortname)
