from django.conf import settings

from main.models import Product


class Like:

    def __init__(self, request):
        self.session = request.session
        like = self.session.get(settings.LIKE_SESSION_ID)
        if settings.LIKE_SESSION_ID not in request.session:
            like = self.session[settings.LIKE_SESSION_ID] = {}
        self.like = like

    def add(self, product):
        product_id = product.id
        if product_id not in self.like:
            self.like[product_id] = {
                'price': str(product.price),
            }

        self.save()

    def __len__(self):
        return len(self.like)

    def __iter__(self):
        product_ids = self.like.keys()
        products = Product.objects.filter(id__in=product_ids)
        like = self.like.copy()

        for product in products:
            like[str(product.id)]['product'] = product

        for item in like.values():
            yield item

    def delete(self, product):
        product_id = str(product)

        if product_id in self.like:
            del self.like[product_id]
            self.save()

    def clear(self):
        del self.session[settings.LIKE_SESSION_ID]
        self.save()

    def save(self):
        self.session.modified = True
