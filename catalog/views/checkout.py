from django import forms    
from django_mako_plus import view_function, jscontext
from datetime import datetime
from django.http import HttpResponseRedirect

@view_function
def process_request(request):

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
           
            return HttpResponseRedirect('/catalog/receipt/')

           # return request.dmp.render('/account/templates/checkout.html')

    # If this is a GET (or any other method) create the default form.
    else:
       
        form = CheckoutForm()

    return request.dmp.render('checkout.html', {
        'form': form,
    })

class CheckoutForm(forms.Form):
    address1 = forms.CharField(label='Address1')
    address2 = forms.CharField(label='Address2')
    city = forms.CharField(label='City')
    state = forms.CharField(label='State')
    zipcode = forms.CharField(label='Zip Code')

    def clean(self):       
        try:
            self.sale.finalize(self.cleaned_data['stripeToken'])
        except Exception as e:
            raise forms.ValidationError('Error processing payment: {}'.format(e))