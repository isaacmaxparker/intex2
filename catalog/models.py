from django.db import models

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
        return self.images_url()[0]

    def images_url(self):
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