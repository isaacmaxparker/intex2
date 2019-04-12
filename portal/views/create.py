from django.contrib.auth import authenticate, login
from django import forms    
from django_mako_plus import view_function, jscontext
from datetime import datetime
from django.http import HttpResponseRedirect
import psycopg2
from django.core.validators import RegexValidator
from homepage import models as rmod
from django.http import HttpResponseRedirect

@view_function
def process_request(request):
    if request.user.has_perm('account.CRUD'):
        # If this is a POST request then process the Form data
        if request.method == 'POST':
            form = CreateForm(request.POST)
                    
            # Check if the form is valid:
            if form.is_valid():

                doc = rmod.Prescribers()
                doc.doctorid = form.cleaned_data.get('doctorid')
                doc.fname = form.cleaned_data.get('firstname')
                doc.lname = form.cleaned_data.get('lastname')
                doc.gender = form.cleaned_data.get('gender')
                doc.state = form.cleaned_data.get('state')
                doc.credentials = form.cleaned_data.get('credentials')
                doc.specialty = form.cleaned_data.get('specialty')
                doc.opioid_prescriber2 = form.cleaned_data.get('isOpiodPres')
                print('---------------------- ABOUT TO SAVE ----------------')
                doc.save()
                print('---------------------- SAVED ----------------')
                doco = rmod.Prescribers.objects.get(doctorid=doc.doctorid )  
                print(doco.doctorid)
                
                return HttpResponseRedirect('/portal/details/' + str(doc.doctorid)+ '/')
                
        # If this is a GET (or any other method) create the default form.
        else:
            form = CreateForm()

            if request.user.has_perm('account.search') or request.user.has_perm('account.safesearch'):
                return request.dmp.render('create.html', {'form': form})
            else:
                return request.dmp.render('error.html') 
    else:
        return request.dmp.render('error.html')
 
class CreateForm (forms.Form):
    GENDERS = (('M', 'Male',), ('F', 'Female',))
    OPTIONS = ((True,'Opiod Prescriber'),(False,'Non-Opiod Prescriber'))
    OCCUPATIONS = (('Addiction Medicine', 'Addiction Medicine'), ('Allergy/Immunology', 'Allergy/Immunology'), ('Anesthesiology', 'Anesthesiology'), ('Behavioral Analyst', 'Behavioral Analyst'), ('CRNA', 'CRNA'), ('Cardiac Electrophysiology', 'Cardiac Electrophysiology'), ('Cardiac Surgery', 'Cardiac Surgery'), ('Cardiology', 'Cardiology'), ('Certified Clinical Nurse Specialist', 'Certified Clinical Nurse Specialist'), ('Certified Nurse Midwife', 'Certified Nurse Midwife'), ('Chiropractic', 'Chiropractic'), ('Clinic/Center', 'Clinic/Center'), ('Clinical Pharmacology', 'Clinical Pharmacology'), ('Colon & Rectal Surgery', 'Colon & Rectal Surgery'), ('Colorectal Surgery (formerly proctology)', 'Colorectal Surgery (formerly proctology)'), ('Community Health Worker', 'Community Health Worker'), ('Counselor', 'Counselor'), ('Critical Care (Intensivists)', 'Critical Care (Intensivists)'), ('Dentist', 'Dentist'), ('Dermatology', 'Dermatology'), ('Diagnostic Radiology', 'Diagnostic Radiology'), ('Emergency Medicine', 'Emergency Medicine'), ('Endocrinology', 'Endocrinology'), ('Family Medicine', 'Family Medicine'), ('Gastroenterology', 'Gastroenterology'), ('General Acute Care Hospital', 'General Acute Care Hospital'), ('General Practice', 'General Practice'), ('General Surgery', 'General Surgery'), ('Geriatric Medicine', 'Geriatric Medicine'), ('Geriatric Psychiatry', 'Geriatric Psychiatry'), ('Gynecological/Oncology', 'Gynecological/Oncology'), ('Hand Surgery', 'Hand Surgery'), ('Health Maintenance Organization', 'Health Maintenance Organization'), ('Hematology', 'Hematology'), ('Hematology/Oncology', 'Hematology/Oncology'), ('Homeopath', 'Homeopath'), ('Hospice and Palliative Care', 'Hospice and Palliative Care'), ('Hospitalist', 'Hospitalist'), ('Infectious Disease', 'Infectious Disease'), ('Internal Medicine', 'Internal Medicine'), ('Interventional Pain Management', 'Interventional Pain Management'), ('Interventional Radiology', 'Interventional Radiology'), ('Legal Medicine', 'Legal Medicine'), ('Licensed Clinical Social Worker', 'Licensed Clinical Social Worker'), ('Licensed Practical Nurse', 'Licensed Practical Nurse'), ('Maxillofacial Surgery', 'Maxillofacial Surgery'), ('Medical Genetics', 'Medical Genetics'), ('Medical Oncology', 'Medical Oncology'), ('Midwife', 'Midwife'), ('Military Health Care Provider', 'Military Health Care Provider'), ('Multispecialty Clinic/Group Practice', 'Multispecialty Clinic/Group Practice'), ('Naturopath', 'Naturopath'), ('Nephrology', 'Nephrology'), ('Neurological Surgery', 'Neurological Surgery'), ('Neurology', 'Neurology'), ('Neuropsychiatry', 'Neuropsychiatry'), ('Neurosurgery', 'Neurosurgery'), ('Nuclear Medicine', 'Nuclear Medicine'), ('Nurse Practitioner', 'Nurse Practitioner'), ('Obstetrics/Gynecology', 'Obstetrics/Gynecology'), ('Ophthalmology', 'Ophthalmology'), ('Optometry', 'Optometry'), ('Oral & Maxillofacial Surgery', 'Oral & Maxillofacial Surgery'), ('Oral Surgery (dentists only)', 'Oral Surgery (dentists only)'), ('Orthopedic Surgery', 'Orthopedic Surgery'), ('Osteopathic Manipulative Medicine', 'Osteopathic Manipulative Medicine'), ('Otolaryngology', 'Otolaryngology'), ('Pain Management', 'Pain Management'), ('Pathology', 'Pathology'), ('Pediatric Medicine', 'Pediatric Medicine'), ('Personal Emergency Response Attendant', 'Personal Emergency Response Attendant'), ('Pharmacist', 'Pharmacist'), ('Pharmacy Technician', 'Pharmacy Technician'), ('Physical Medicine and Rehabilitation', 'Physical Medicine and Rehabilitation'), ('Physical Therapist', 'Physical Therapist'), ('Physician Assistant', 'Physician Assistant'), ('Plastic Surgery', 'Plastic Surgery'), ('Podiatry', 'Podiatry'), ('Preferred Provider Organization', 'Preferred Provider Organization'), ('Preventive Medicine', 'Preventive Medicine'), ('Psychiatry', 'Psychiatry'), ('Psychiatry & Neurology', 'Psychiatry & Neurology'), ('Psychologist', 'Psychologist'), ('Pulmonary Disease', 'Pulmonary Disease'), ('Radiation Oncology', 'Radiation Oncology'), ('Registered Nurse', 'Registered Nurse'), ('Rehabilitation Agency', 'Rehabilitation Agency'), ('Rheumatology', 'Rheumatology'), ('Sleep Medicine', 'Sleep Medicine'), ('Slide Preparation Facility', 'Slide Preparation Facility'), ('Sports Medicine', 'Sports Medicine'), ('Student in an Organized Health Care Education/Training Program', 'Student'), ('Surgery', 'Surgery'), ('Surgical Oncology', 'Surgical Oncology'), ('Thoracic Surgery', 'Thoracic Surgery'), ('Other', 'Other'), ('Urology', 'Urology'), ('Vascular Surgery', 'Vascular Surgery'), ('Other', 'Other'))
    STATES=(('AL', 'Alabama '), ('AK', 'Alaska '), ('AZ', 'Arizona '), ('AR', 'Arkansas '), ('CA', 'California '), ('CO', 'Colorado '), ('CT', 'Connecticut '), ('DE', 'Delaware '), ('FL', 'Florida '), ('GA', 'Georgia '), ('HI', 'Hawaii '), ('ID', 'Idaho '), ('IL', 'Illinois '), ('IN', 'Indiana '), ('IA', 'Iowa '), ('KS', 'Kansas '), ('KY', 'Kentucky '), ('LA', 'Louisiana '), ('ME', 'Maine '), ('MD', 'Maryland '), ('MA', 'Massachusetts '), ('MI', 'Michigan '), ('MN', 'Minnesota '), ('MS', 'Mississippi '), ('MO', 'Missouri '), ('MT', 'Montana '), ('NE', 'Nebraska '), ('NV', 'Nevada '), ('NH', 'New '), ('NJ', 'New '), ('NM', 'New '), ('NY', 'New '), ('NC', 'North '), ('ND', 'North '), ('OH', 'Ohio '), ('OK', 'Oklahoma '), ('OR', 'Oregon '), ('PA', 'Pennsylvania '), ('RI', 'Rhode '), ('SC', 'South '), ('SD', 'South '), ('TN', 'Tennessee '), ('TX', 'Texas '), ('UT', 'Utah '), ('VT', 'Vermont '), ('VA', 'Virginia '), ('WA', 'Washington '), ('WV', 'West '), ('WI', 'Wisconsin '), ('WY', 'Wyoming '))
    OPTIONS = ((True,'Opiod Prescriber'),(False,'Non-Opiod Prescriber'))
        
    doctorid = forms.CharField(label='Doctor ID', required=True)
    firstname = forms.CharField(label='First Name', required=True)
    lastname = forms.CharField(label='Last Name', required=True )
    gender = forms.ChoiceField(label='Gender',choices=GENDERS, required=True)
    state = forms.ChoiceField(label='Location',choices=STATES, required=True)
    credentials = forms.CharField(label='Credentials',required=True)
    specialty = forms.ChoiceField(label='Specialty',choices=OCCUPATIONS, required=True)
    isOpiodPres = forms.ChoiceField(label='Location',choices=OPTIONS, required=True)
        
    def clean(self):
            return self.cleaned_data


