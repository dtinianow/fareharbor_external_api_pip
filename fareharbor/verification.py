class Verification(object):
    def __init__(self, params):
        for key in params:
            setattr(self, key, params[key])
