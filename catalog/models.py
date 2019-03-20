from django.db import models
from decimal import Decimal

# Create your models here.
class Category(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField(default='')


class Product(models.Model):

    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )

    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.TextField(db_index=True, choices=STATUS_CHOICES, default='A')
    name = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.IntegerField(default=1)
    reorder_trigger = models.IntegerField(default=1)
    reorder_quantity = models.IntegerField(default=1)

    def image_url(self):
        ''
        return self.image_urls()[0]

    def image_urls(self):
        urls = []
        for pi in ProductImage.objects.filter(product=self):
            urls.append(pi.image_url())
        # if list is empty append no iimage available
        if len(urls) == 0:
            urls.append('/static/catalog/media/products/noimage.png')
        return urls
    
class ProductImage(models.Model):
    'an image for a product'
    filename = models.TextField(default='noimage.png')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')

    def image_url(self):
        return '/static/catalog/media/products/' + self.filename


class Sale(models.Model):
        user = models.ForeignKey("account.User", on_delete=models.PROTECT)
        created = models.DateTimeField(auto_now_add=True)
        purchased = models.DateTimeField(null=True, default=None)
        subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
        tax = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
        total = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
        charge_id = models.TextField(null=True, default=None)   # successful charge id from stripe

        def recalculate(self):
            '''Recalculates the subtotal, tax, and total fields. Does not save the object.'''
            sales = SaleItem.objects.filter(product=self, status='A')
            for sale in sales:
                sub += sale.price
            self.subtotal = sub
            self.tax = self.subtotal * .05
            self.total = self.subtotal + self.tax

        def finalize(self, stripeToken):
            '''Finalizes the sale'''
            # complete this method!
            # Ensure this sale isn't already finalized (purchased should be None)
            if self.purchased is not None:
                raise ValueError("This sale has already been finalized")
            
            # Check product quantities one more time
            # if self.quantity <= self.product.quantity
            #     raise ValueError("Not enough in stock!")
            # Call recalculate one more time
            self.recalculate()
            # Create a charge using the `stripeToken` (https://stripe.com/docs/charges)
                # be sure to pip install stripe and import stripe into this file
            # Set purchased=now and charge_id=the id from Stripe
            self.purchased = now
            # self.charge_id=
            # Save

class SaleItem(models.Model):
        STATUS_CHOICES = [
            ( 'A', 'Active' ),
            ( 'D', 'Deleted' ),
        ]
        status = models.CharField(max_length=1, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
        sale = models.ForeignKey("Sale", on_delete=models.PROTECT, related_name="items")
        product = models.ForeignKey("Product", on_delete=models.PROTECT)
        quantity = models.IntegerField(default=0)
        price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
        class Meta:
            ordering = [ 'product__name' ]