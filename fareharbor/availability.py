class Availability(object):

    def __init__(self, availability):
        for key in availability:
            setattr(self, key, availability[key])
