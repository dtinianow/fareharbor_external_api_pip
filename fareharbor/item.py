class Item:
    def __init__(self, params):
        import code; code.interact(local=dict(globals(), **locals()))
        for key in params:
            setattr(self, key, params[key])
