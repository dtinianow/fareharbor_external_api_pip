class Item(object):

    def __init__(self, item):
        for key in item:
            setattr(self, key, item[key])
