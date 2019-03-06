from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
from django.http import HttpResponse

@view_function
def process_request(request, product:cmod.Product):

    context = {
        
        'name':product.name,
        'price':product.price,
        'desc':product.description,
        'imageurls':product.images_url(),
        'quant':product.quantity

    }
    return request.dmp.render('product.html', context)

@view_function
def tile(request, product:cmod.Product):
    return request.dmp.render('product.tile.html', {
        'product':product
    })
