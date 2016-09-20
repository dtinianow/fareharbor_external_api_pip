class Lodging:
    
    def __init__(self, lodging):
        self.name            = lodging['name']
        self.is_self_lodging = lodging['is_self_lodging']
        self.url             = lodging['url']
        self.phone           = lodging['phone']
        self.address         = lodging['address']
        self.pk              = lodging['pk']
