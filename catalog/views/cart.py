from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from catalog import models as cmod

@view_function
def process_request(request):
    context = {
       
    }
    return request.dmp.render('cart.html', context)

@view_function
def remove(request):
    context = {
       
    }
    return request.dmp.render('cart.html', context)