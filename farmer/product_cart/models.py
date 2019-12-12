from django.db import models
from user_profile.models import Product
from django.conf import settings


#if user is the farmer
from farmer_page.models import Farmer




class orderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return self.item.product_name
    

class order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(orderItem)
    creationDate = models.DateTimeField(auto_now_add=True)
    orderedDate = models.DateTimeField()
    total = models.FloatField()

    def __str__(self):
        return self.user.username

    @property
    def total_price(self):
        return self.orderItem_set.aggregate(
            total_price=Sum(F('quantity') * F('Product__price'))
        )['total_price'] or Decimal('0')

