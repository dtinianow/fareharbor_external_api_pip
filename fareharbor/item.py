class Item:

    def __init__(self, item):
        self.image_cdn_url                 = item['image_cdn_url']
        self.name                          = item['name']
        self.cancellation_policy_safe_html = item['cancellation_policy_safe_html']
        self.headline                      = item['headline']
        self.cancellation_policy           = item['cancellation_policy']
        self.is_pickup_ever_available      = item['is_pickup_ever_available']
        self.description_safe_html         = item['description_safe_html']
        self.location                      = item['location']
        self.customer_prototypes           = item['customer_prototypes']
        self.images                        = item['images']
        self.pk                            = item['pk']
        self.tax_percentage                = item['tax_percentage']
        self.description                   = item['description']
