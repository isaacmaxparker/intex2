from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime
from django.test import TestCase
from account import models as amod
from django import forms
from django.contrib.auth import authenticate, login

@view_function
def process_request(request):

    if request.method =='POST':
        form = PassForm(request.POST)
        if form.is_valid():
            uname = request.user.username
            passphrase = form.cleaned_data.get('password')
            current = amod.User.objects.get(username=uname)
            current.set_password(passphrase)
            current.save()
            user = authenticate(username=uname,password=passphrase)
            login(request,user)

            context = {
            'form':form,
            'msg':'Password Changed'
            }
            return request.dmp.render('changepass.html',context)
    else:
        form = PassForm()
        context = {
            'form':form,
            'msg':''
            }
        return request.dmp.render('changepass.html',context)

class PassForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(), label='New Password',required=True,min_length=14)
    

    def clean(self):
        return self.cleaned_data
        
       
