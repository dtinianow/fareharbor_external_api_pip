class Verification(object):

    def __init__(self, verification):
        for key in verification:
            setattr(self, key, verification[key])
