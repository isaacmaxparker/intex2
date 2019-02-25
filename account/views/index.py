from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime
from django.test import TestCase
from account import models as amod

@view_function
def process_request(request):


        return request.dmp.render('index.html')
