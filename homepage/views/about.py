from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime
from django.views.decorators.clickjacking import xframe_options_deny

@xframe_options_deny
@view_function
def process_request(request):
    return request.dmp.render('about.html')