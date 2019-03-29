from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod
from django.http import HttpResponseRedirect

@view_function
def process_request(request, product:cmod.Product):
    sale5 = request.user.get_shopping_cart()
    try:
        saleitem = cmod.SaleItem.objects.get(sale = sale5, product = product)
        quantincart = saleitem.quantity
    except:
        quantincart = 0

    if request.method == 'POST': 
        if request.user.is_authenticated == False:
            return HttpResponseRedirect('/account/login/')
        
        quantwant = int(request.POST['QuantOrd'])

        if quantwant > (product.quantity - quantincart):
            context = {
                'name':product.name,
                'price':product.price,
                'desc':product.description,
                'imageurls':product.image_urls(),
                'quant':product.quantity,
                'message':'Not Enough in stock'
            }
            return request.dmp.render('product.html', context)
        print(quantwant)
        if quantwant == 0:
            context = {
                'name':product.name,
                'price':product.price,
                'desc':product.description,
                'imageurls':product.image_urls(),
                'quant':product.quantity,
                'message':'Select at least one item'
            }
            return request.dmp.render('product.html', context)

        sale5 = request.user.get_shopping_cart()
        
        try:
             saleitem = cmod.SaleItem.objects.get(sale = sale5, product = product, status = 'A')
             saleitem.quantity += quantwant
             saleitem.save()
        except:
            thisSale = cmod.SaleItem()
            thisSale.sale = sale5
            thisSale.product = product
            thisSale.quantity = quantwant
            thisSale.price = product.price
            thisSale.save()
                
        return HttpResponseRedirect('/catalog/cart/')

    context = {
        
        'name':product.name,
        'price':product.price,
        'desc':product.description,
        'imageurls':product.image_urls(),
        'quant':product.quantity,
        'message':''

    }
    return request.dmp.render('product.html', context)

@view_function
def tile(request, product:cmod.Product):
    return request.dmp.render('product.tile.html', {
        'product':product
    })
