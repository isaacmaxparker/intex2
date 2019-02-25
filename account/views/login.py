from django.contrib.auth import authenticate, login
from django import forms    
from django_mako_plus import view_function, jscontext
from datetime import datetime
from django.http import HttpResponseRedirect

@view_function
def process_request(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))     
            login(request, user)
            return HttpResponseRedirect('/')

           # return request.dmp.render('/account/templates/login.html')

    # If this is a GET (or any other method) create the default form.
    else:
       
        form = LoginForm()

    return request.dmp.render('login.html', {
        'form': form,
    })

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    
    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))        
        if user is None:
            raise forms.ValidationError('Invalid Credentials')
        return self.cleaned_data