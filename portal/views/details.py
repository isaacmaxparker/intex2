from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as rmod
import requests
import json

@view_function
def process_request(request, docid ):
    if request.user.has_perm('account.search') or request.user.has_perm('account.safesearch'):
        try:
            recom = rmod.Drug_Quant_Rec.objects.get(doctorid = docid)
            prescrecom = True
        except:
            recom = rmod.Drug_Quant_Rec.objects.all()[67]
            prescrecom = False
        doc = rmod.Prescribers.objects.get(doctorid = docid)
        state = rmod.Overdoses.objects.get(abbrev = doc.state)
        
        try:
            opiates = rmod.Prescriptions.objects.get(doctorid = docid)
        except:
            opiates = 'NONE'
        try:
            risk = rmod.Prescription_Risk.objects.get(doctorid = docid)
        except:
            risk= 'NONE'

        if request.user.has_perm('account.search'):
            fullname = doc.fname + ' ' +  doc.lname
        elif request.user.has_perm('account.safesearch'):
            fullname = doc.doctorid

        

        url = "https://ussouthcentral.services.azureml.net/workspaces/f51467e7b4c24d6da796acaa6fc7de7d/services/1a8b1e7f283e42538385336a6b5ec906/execute"

        querystring = {"api-version":"2.0","details":"true"}

        payload = '{\n  \"Inputs\": {\n    \"input1\": {\n      \"ColumnNames\": [\n        \"DoctorID\",\n        \"Drug\",\n        \"Qty\"\n      ],\n      \"Values\": [\n        [\n          \"' + doc.doctorid + '\",\n          \"value\",\n          \"0\"\n        ]\n      ]\n    }\n  },\n  \"GlobalParameters\": {}\n}'
        headers = {
        'Authorization': "bearer xC0GHohrIZEFitWBMAq7aFBpZTbrrurwcE8mVt+bd0Sb1lQBjrTUVsC0nBWJXK5avMRsrTozMmycMVQ8ul9WqQ==",
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "39f69417-9ec4-46ca-899b-a0991808ec0f"
        }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
        results = response.text
        prediction = str(results)
        prediction = prediction.replace("{", "").replace("}", "").replace("]", "").replace("[", "")
        prediction = prediction.replace("Results", "").replace("String", "").replace(":", "").replace('"', "")
        prediction = prediction.replace("output1typetable,valueColumnNamesRelated User 1,Related User 2,Related User 3,Related User 4,Related User 5,ColumnTypes,,,,,Values", "").replace(',', "")
      

        relatives = list()
        while len(prediction) > 0:
            docid = prediction[:10]
            prediction = prediction[10:]
            try:
                doco = rmod.Prescribers.objects.get(doctorid=docid)
            except:
                doco = 'NONE'
            relatives.append(doco)
        
        relatives=relatives[:5]
        statename = rmod.Overdoses.objects.get(abbrev=doc.state)

        context={
            'id':doc.doctorid,
            'gender':doc.gender,
            'fullname':fullname,
            'specialty':doc.specialty,
            'sellsOpiod':doc.opioid_prescriber2,
            'state':doc.state,
            'statename':statename.state,
            'deaths':state.deaths,
            'opiates':opiates,
            'relatives':relatives, 
            'risk': risk.rating if risk != 'NONE' else 'NONE',
            'prescless':recom.presc_less,
            'prescmore':recom.presc_more,
            'prescrecom':prescrecom,
        }
        return request.dmp.render('prescriberdetails.html',context)
    else:
        return request.dmp.render('error.html') 

    