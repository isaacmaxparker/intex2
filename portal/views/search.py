from django.contrib.auth import authenticate, login
from django import forms    
from django_mako_plus import view_function, jscontext
from datetime import datetime
from django.http import HttpResponseRedirect
import psycopg2
from django.core.validators import RegexValidator
from account import models as amod

@view_function
def process_request(request):

 
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = SearchForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            providers = amod.User.objects.filter(first_name=form.cleaned_data.get('firstname'))
            providers = amod.User.objects.all()
            context = {
                'providers':providers
            }           
            return request.dmp.render('results.html', context)
            
           # return request.dmp.render('/account/templates/login.html')

    # If this is a GET (or any other method) create the default form.
    else:
        form = SearchForm()
        if request.user.has_perm('account.search'):
           return request.dmp.render('search.html', {'form': form,})
        else:
            if request.user.has_perm('account.safesearch'):
                return request.dmp.render('search.html', {'form': form,})
            else:
                return request.dmp.render('error.html')   

class SearchForm(forms.Form):
    CHOICES = (('M', 'Male',), ('F', 'Female',))
    my_validator = RegexValidator("^(?-i:A[LKSZRAEP]|C[AOT]|D[EC]|F[LM]|G[AU]|HI|I[ADLN]|K[SY]|LA|M[ADEHINOPST]|N[CDEHJMVY]|O[HKR]|P[ARW]|RI|S[CD]|T[NX]|UT|V[AIT]|W[AIVY])$", "Your string should contain letter A in it.")


    firstname = forms.CharField(label='First Name', required=False)
    lastname = forms.CharField(label='Last Name',required=False )
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES, required=False)
    state = forms.CharField(label='State', max_length=2, validators=[my_validator] , required=False)
    specialty = forms.ChoiceField(choices=CHOICES, required=False)
    
        