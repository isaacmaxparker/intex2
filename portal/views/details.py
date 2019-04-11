from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from portal import models as rmod

@view_function
def process_request(request, docid ):
    if request.user.has_perm('account.search') or request.user.has_perm('account.safesearch'):
        #state=rmod.Overdoses.objects.get(abbrev=doc.state)
        doc = rmod.Prescribers.objects.get(doctorid = docid)
        if request.user.has_perm('account.search'):
            fullname = doc.fname + ' ' +  doc.lname
        elif request.user.has_perm('account.safesearch'):
            fullname = doc.doctorid

        context={
            'gender':doc.gender,
            'fullname':fullname,
            'specialty':doc.specialty,
            'sellsOpiod':doc.opioid_prescriber2,
            'state':doc.state,
            'deaths':567
        }
        return request.dmp.render('prescriberdetails.html',context)
    else:
        return request.dmp.render('error.html') 

    