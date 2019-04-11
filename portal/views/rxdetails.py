from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from account import models as amod

@view_function
def process_request(request, rx:amod.User):
    if request.user.has_perm('account.search') or request.user.has_perm('account.safesearch'):
            isOpiod = True
            context={
                'rxName':rx.first_name + '56789012345678901234567890',
                'isOpiod':isOpiod,
                'rxPercent':'67%',   
                'rxImage':'opiods' if isOpiod else 'leafpill',
            }
            return request.dmp.render('rxdetails.html', context )
    else:
            return request.dmp.render('error.html') 