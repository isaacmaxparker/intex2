from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
from django.http import HttpResponseRedirect

@view_function
def process_request(request): 
    sale = request.user.get_shopping_cart()
    sale.recalculate()
    saleItems = cmod.SaleItem.objects.filter(sale=sale, status = 'A')
    
    context = {
       'total':sale.total,
       'subtotal':sale.subtotal,
       'tax':sale.tax,
       'saleItems':saleItems,
       'cart':sale,
    }
    return request.dmp.render('cart.html', context)

@view_function
def remove(request, product:cmod.Product):
    sale = request.user.get_shopping_cart()
    saleItem = cmod.SaleItem.objects.get(sale=sale, product=product)
    saleItem.status = 'D'
    saleItem.save()
    return HttpResponseRedirect('/catalog/cart/')