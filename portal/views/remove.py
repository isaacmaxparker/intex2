from django.contrib.auth import authenticate, login
from django import forms    
from django_mako_plus import view_function, jscontext
from datetime import datetime
from django.http import HttpResponseRedirect
import psycopg2
from django.core.validators import RegexValidator
from homepage import models as rmod

@view_function
def process_request(request, docid):
    try:
        prescriber = rmod.Prescribers.objects.get(doctorid=docid)
        exists = True
    except:
        exists = False
        
    if request.method == 'POST':
        form = RemoveForm(request.POST)
        # Check if the form is valid:
        if form.is_valid() and exists == True:
            try:
                prescriber.delete()
            except:
                exists = False
            exists = False
            context={
                'form':RemoveForm(),
                'exists': exists,
                'gender':'question',
                'name':'Removed',
                'msg':'Prescriber Deleted',
            }
            return request.dmp.render('remove.html', context)

    
    elif exists == True:
        form = RemoveForm()

        context = {
            'form':form,
            'exists':exists,
            'gender':'Female' if prescriber.gender == 'F' else 'Male',
            'name':prescriber.fname + ' ' + prescriber.lname,
            'msg':'Are you sure you want to delete this prescriber?',
        }
        return request.dmp.render('remove.html',context)
    else:
        form = RemoveForm()

        context={
                'form':RemoveForm(),
                'exists': exists,
                'gender':'pill',
                'name':'Removed',
                'msg':'Prescriber does not exist',
            }
        return request.dmp.render('remove.html', context)

class RemoveForm (forms.Form):
        confirmation = forms.CharField(label='', required=True)
        
        def clean(self):
            if self.cleaned_data.get('confirmation') == 'Delete':
                return self.cleaned_data
            else:
                return forms.ValidationError('Confirmation failed')