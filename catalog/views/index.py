from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod


ITEMS_PAGE_PAGE = 3


@view_function
def process_request(request, category:cmod.Category=None, page:int=1):

    products = cmod.Product.objects.filter(status="A")

    if category is not None:
        products=products.filter(category=category)

    products= products[(page - 1) * ITEMS_PAGE_PAGE: page * ITEMS_PAGE_PAGE]

    context = {
        'category':category,
        'products':products,
        'page':page,
        'numpages': math.ceil(products.count()/ITEMS_PAGE_PAGE),
       
    }
    return request.dmp.render('index.html', context)