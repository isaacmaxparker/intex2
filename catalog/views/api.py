from django_mako_plus import view_function, jscontext
from django.http import HttpResponse

@view_function
def process_request(request):

#return HttpResponse("Hey Hey Hey")

    return request.dmp.render('api.html', {})

@view_function
def getdata(request):

    return HttpResponse("Hey Hey Hey")