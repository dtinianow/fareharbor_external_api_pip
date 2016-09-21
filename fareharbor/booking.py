class Booking(object):

    def __init__(self, booking):
        for key in booking:
            setattr(self, key, booking[key])
