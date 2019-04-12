from django.contrib.auth import authenticate, login
from django import forms    
from django_mako_plus import view_function, jscontext
from datetime import datetime
from django.http import HttpResponseRedirect
from django.core.validators import RegexValidator
from homepage import models as rmod

@view_function
def process_request(request, docid):
    if request.user.has_perm('account.CRUD'):
        prescription = rmod.Prescriptions.objects.get(doctorid=docid)
        if request.method == 'POST':
            form = UpdateForm(request.POST)
            
            prescription = rmod.Prescriptions.objects.get(doctorid=docid)
            print('--------------------- ZERO')
            # Check if the form is valid:
            if form.is_valid():
                print('--------------------- ONE')
                prescription = rmod.Prescriptions.objects.get(doctorid=docid)
                prescription.acetaminophen_codeine=form.cleaned_data.get('acetaminophen_codeine')
                prescription.fentanyl=form.cleaned_data.get('fentanyl')
                prescription.hydrocodone_acetaminophen=form.cleaned_data.get('hydrocodone_acetaminophen')
                prescription.hydromorphone_hcl=form.cleaned_data.get('hydromorphone_hcl')
                prescription.methadone_hcl=form.cleaned_data.get('methadone_hcl')
                prescription.morphine_sulfate=form.cleaned_data.get('morphine_sulfate')
                prescription.morphine_sulfate_er=form.cleaned_data.get('morphine_sulfate_er')
                prescription.fentanyl=form.cleaned_data.get('fentanyl')
                prescription.fentanyl=form.cleaned_data.get('fentanyl')
                prescription.fentanyl=form.cleaned_data.get('fentanyl')
                prescription.fentanyl=form.cleaned_data.get('fentanyl')
                print('--------------------- ONE')
                print(prescription2.acetaminophen_codeiene)
                print('--------------------- TWO')
                print(form.cleaned_data.get('acetaminophen_codeine'))

                prescription.save()

                prescription2 = rmod.Prescriptions.objects.get(doctorid=docid) 

                print(prescription2.acetaminophen_codeiene)


                context={
                    'form':UpdateForm(initial={'acetaminophen_codeine': prescription.acetaminophen_codeine,'fentanyl':prescription.fentanyl,'hydrocodone_acetaminophen':prescription.hydrocodone_acetaminophen,'hydromorphone_hcl':prescription.hydromorphone_hcl,'methadone_hcl':prescription.methadone_hcl,'morphine_sulfate':prescription.morphine_sulfate, 'morphine_sulfate_er':prescription.morphine_sulfate_er, 'oxycodone_acetaminophen':prescription.oxycodone_acetaminophen,'oxycodone_hcl':prescription.oxycodone_hcl, 'oxycontin':prescription.oxycontin,'tramadol_hcl':prescription.tramadol_hcl})
                    ,'doctorid':prescription.doctorid
                }
                return request.dmp.render('update.html', context)

        form = UpdateForm(initial={'acetaminophen_codeine': prescription.acetaminophen_codeine,'fentanyl':prescription.fentanyl,'hydrocodone_acetaminophen':prescription.hydrocodone_acetaminophen,'hydromorphone_hcl':prescription.hydromorphone_hcl,'methadone_hcl':prescription.methadone_hcl,'morphine_sulfate':prescription.morphine_sulfate, 'morphine_sulfate_er':prescription.morphine_sulfate_er, 'oxycodone_acetaminophen':prescription.oxycodone_acetaminophen,'oxycodone_hcl':prescription.oxycodone_hcl, 'oxycontin':prescription.oxycontin,'tramadol_hcl':prescription.tramadol_hcl})

        context = {
            'form':form
            ,'doctorid':prescription.doctorid
        }
        return request.dmp.render('update.html',context)
    else:
        return request.dmp.render('error.html')

class UpdateForm (forms.Form):
    acetaminophen_codeine = forms.DecimalField(max_digits=7,decimal_places=6)
    fentanyl  = forms.DecimalField(max_digits=7,decimal_places=6)
    hydrocodone_acetaminophen = forms.DecimalField(max_digits=7,decimal_places=6)
    hydromorphone_hcl = forms.DecimalField(max_digits=7,decimal_places=6)
    methadone_hcl = forms.DecimalField(max_digits=7,decimal_places=6)
    morphine_sulfate = forms.DecimalField(max_digits=7,decimal_places=6)
    morphine_sulfate_er = forms.DecimalField(max_digits=7,decimal_places=6)
    oxycodone_acetaminophen = forms.DecimalField(max_digits=7,decimal_places=6)
    oxycodone_hcl = forms.DecimalField(max_digits=7,decimal_places=6)
    oxycontin = forms.DecimalField(max_digits=7,decimal_places=6)
    tramadol_hcl = forms.DecimalField(max_digits=7,decimal_places=6)

    def clean(self):
        return self.cleaned_data