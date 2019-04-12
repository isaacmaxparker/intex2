from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from homepage import models as rmod

@view_function
def process_request(request, rx:rmod.Opiods_Related):
    if request.user.has_perm('account.search') or request.user.has_perm('account.safesearch'):
            perc = rx.OverPresc *100
            perc = str(perc)
            perc = perc[:4]
            perc += '%'
            name_link = str(rx.name_link)
            print(name_link)
            try:
                if name_link == 'acetmin_high':
                    topguys = rmod.High_Presc.objects.filter(acetmin_high = 1)[:5]
                    onlyguys = rmod.High_Presc.objects.filter(acetmin_high = 2)[:5]
                else:
                    if name_link == 'fenty_high':
                        topguys = rmod.High_Presc.objects.filter(fenty_high = 1)[:5]
                        onlyguys = rmod.High_Presc.objects.filter(fenty_high = 2)[:5]
                    else:
                        if name_link == 'hydro_aceta_high':
                            topguys = rmod.High_Presc.objects.filter(hydro_aceta_high = 1)[:5]
                            onlyguys = rmod.High_Presc.objects.filter(hydro_aceta_high = 2)[:5]
                        else:
                            if name_link == 'hydromorphone_high':
                                topguys = rmod.High_Presc.objects.filter(hydromorphone_high = 1)[:5]
                                onlyguys = rmod.High_Presc.objects.filter(hydromorphone_high = 2)[:5]
                            else:
                                if name_link == 'methadone_high':
                                    topguys = rmod.High_Presc.objects.filter(methadone_high = 1)[:5]
                                    onlyguys = rmod.High_Presc.objects.filter(methadone_high = 2)[:5]
                                else:
                                    if name_link == 'morphine_high':
                                        topguys = rmod.High_Presc.objects.filter(morphine_high = 1)[:5]
                                        onlyguys = rmod.High_Presc.objects.filter(morphine_high = 2)[:5]
                                    else:
                                        if name_link == 'morphine_ext_high':
                                            topguys = rmod.High_Presc.objects.filter(morphine_ext_high = 1)[:5]
                                            onlyguys = rmod.High_Presc.objects.filter(morphine_ext_high = 2)[:5]
                                        else:
                                            if name_link == 'oxy_aceta_high':
                                                topguys = rmod.High_Presc.objects.filter(oxy_aceta_high = 1)[:5]
                                                onlyguys = rmod.High_Presc.objects.filter(oxy_aceta_high = 2)[:5]
                                            else:
                                                if name_link == 'oxy_hcl_high':
                                                    topguys = rmod.High_Presc.objects.filter(oxy_hcl_high = 1)[:5]
                                                    onlyguys = rmod.High_Presc.objects.filter(oxy_hcl_high = 2)[:5]
                                                else:
                                                    if name_link == 'oxycotin_high':
                                                        topguys = rmod.High_Presc.objects.filter(oxycotin_high = 1)[:5]
                                                        onlyguys = rmod.High_Presc.objects.filter(oxycotin_high = 2)[:5] 
                                                    else:      
                                                        if name_link == 'tramadol_high':
                                                            topguys = rmod.High_Presc.objects.filter(tramadol_high = 1)[:5]
                                                            onlyguys = rmod.High_Presc.objects.filter(tramadol_high = 2)[:5]
                                                        else:
                                                            topguys = rmod.High_Presc.objects.all()[:5]
                                                            onlyguys = rmod.High_Presc.objects.all()[:5]
            except:
        
                    topguys = rmod.High_Presc.objects.all()[:5]
                    onlyguys = rmod.High_Presc.objects.all()[:5]
                




            guys = list()
            guys2 = list()
            try:
                for item in topguys:
                    guys.append(rmod.Prescribers.objects.get(doctorid=item.doctorid))
                for item in onlyguys:
                    guys2.append(rmod.Prescribers.objects.get(doctorid=item.doctorid))
            except:
                guys = ''
                guys2 = ''


            context={
                'rxName':rx.drugName,
                'isOpiod':rx.isOpioid,
                'rxPercent':perc,   
                'rxImage':'opiods' if rx.isOpioid else 'leafpill',
                'topguys':guys,
                'onlyguys':guys2,
            }
            return request.dmp.render('rxdetails.html', context )
    else:
            return request.dmp.render('error.html') 