from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from account import models as amod

@view_function
def process_request(request, doc:amod.User ):
    if request.user.has_perm('account.search') or request.user.has_perm('account.safesearch'):
        context={
            'gender':'Female',
            'fullname':doc.first_name + ' ' +  doc.last_name,
            'specialty':'Dentist asdf asdf asd fa sdf asd ',
            'sellsOpiod':False,
            'state':'UT'
        }
        return request.dmp.render('prescriberdetails.html',context)
    else:
        return request.dmp.render('error.html') 

    