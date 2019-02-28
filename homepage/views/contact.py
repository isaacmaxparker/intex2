from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime

@view_function
def process_request(request):

    if request.method == 'POST':
        #check variables -- assume the worst
        print("Name is " + request.POST['yourname'])
        print("Email is " + request.POST['youremail'])
        print("Message: " + request.POST['yourmessage'])
        #if user does it right
        #do the work
        #return HTTPResponseRedirect('/somewhere/else/')
        
        context = {
            'msg': "Thank you for submitting your form",
        }

        return request.dmp.render('contact.html', context)

    else:

        context = {
             'msg': "",
        }

        return request.dmp.render('contact.html', context)