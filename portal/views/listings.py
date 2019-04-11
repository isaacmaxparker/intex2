from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django.http import HttpResponseRedirect

@view_function
def process_request(request):

    if request.user.has_perm('account.CRUD') or request.user.has_perm('account.CRUD'):
            return request.dmp.render('listing.html')
    else:
            return request.dmp.render('error.html') 