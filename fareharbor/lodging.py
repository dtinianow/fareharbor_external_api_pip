class Lodging(object):

    def __init__(self, lodging):
        for key in lodging:
            setattr(self, key, lodging[key])
