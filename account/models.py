from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog import models as cmod

# Create your models here.
class User(AbstractUser):
    birthdate=models.DateTimeField(null = True)

    def get_shopping_cart(self):
            from catalog import models as cmod
            # retrieve (or create) a Sale with purchased=None for this user
            
            try:
                sale = cmod.Sale.objects.get(user=self, purchased=None)
            except:
                sale = cmod.Sale()
                sale.user = self
                sale.save()
                print('--------------------')
                print(sale.user)

            # return the Sale object
            return sale