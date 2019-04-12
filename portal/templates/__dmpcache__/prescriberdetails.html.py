# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555048283.7464013
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/portal/templates/prescriberdetails.html'
_template_uri = 'prescriberdetails.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'left_content', 'site_content', 'right_content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        prescrecom = context.get('prescrecom', UNDEFINED)
        prescless = context.get('prescless', UNDEFINED)
        state = context.get('state', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        relatives = context.get('relatives', UNDEFINED)
        specialty = context.get('specialty', UNDEFINED)
        risk = context.get('risk', UNDEFINED)
        fullname = context.get('fullname', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        deaths = context.get('deaths', UNDEFINED)
        gender = context.get('gender', UNDEFINED)
        prescmore = context.get('prescmore', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        sellsOpiod = context.get('sellsOpiod', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        statename = context.get('statename', UNDEFINED)
        opiates = context.get('opiates', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('&mdash; Home')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        prescrecom = context.get('prescrecom', UNDEFINED)
        prescless = context.get('prescless', UNDEFINED)
        state = context.get('state', UNDEFINED)
        relatives = context.get('relatives', UNDEFINED)
        specialty = context.get('specialty', UNDEFINED)
        risk = context.get('risk', UNDEFINED)
        fullname = context.get('fullname', UNDEFINED)
        def site_content():
            return render_site_content(context)
        deaths = context.get('deaths', UNDEFINED)
        gender = context.get('gender', UNDEFINED)
        prescmore = context.get('prescmore', UNDEFINED)
        sellsOpiod = context.get('sellsOpiod', UNDEFINED)
        statename = context.get('statename', UNDEFINED)
        opiates = context.get('opiates', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n   <div class="content">\r\n      <table class="detstab">\r\n         <tr>\r\n            <td>\r\n                  <img src="/static/homepage/media/UserImages/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('Male' if gender == 'M' else 'Female'))
        __M_writer('.png">\r\n            </td>\r\n            <td class="bio">\r\n                  <p class="name" style="line-height: 56px;">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(fullname))
        __M_writer('<span class="info" style="margin-left:40px; font-weight:100;">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('Female' if gender == 'F' else 'Male'))
        __M_writer('</span></p>\r\n                  <p class="spec" style="font-weight: bold;">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(specialty))
        __M_writer(' <span style="margin-left:60px; font-weight:100; ">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(statename))
        __M_writer('</span></p>\r\n                  <p class="info"><span class="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('red' if sellsOpiod else ''))
        __M_writer('">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('Opiate Prescriber' if sellsOpiod else 'Non-Opiate Prescriber' ))
        __M_writer('</span></p>\r\n')
        if prescrecom:
            __M_writer('                  <p>We recommend ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(fullname))
            __M_writer(' prescribe less of <span style="color:red;font-weight:bold">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescless))
            __M_writer('</span> and instead prescribe more <span style="color:rgb(15, 173, 15);font-weight:bold">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescmore))
            __M_writer('</span></p>\r\n')
        __M_writer('            </td>\r\n            <td style="width:0px;border-right-style:solid;border-color:rgb(189, 189, 189);border-width:1px; padding:10px;"></td>\r\n            <td style="vertical-align:middle; padding-left:40px;">\r\n               <p class="stat" style="font-size:60px;line-height: 30px;">\r\n                  ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(deaths))
        __M_writer('\r\n               </p>\r\n               <p style="font-size:20px;">\r\n                  opiod-related <br>deaths in <span style="font-size:35px;"><b>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(state))
        __M_writer('</b></span>\r\n               </p>\r\n               <!-- <p>Recommendations:</p>\r\n               <p>Prescribe more of ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescmore))
        __M_writer('</p>\r\n               <p>Prescribe less of ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(prescless))
        __M_writer('</p> -->\r\n               \r\n            </td>\r\n         </tr>\r\n      </table>\r\n')
        if request.user.has_perm('account.search') and risk != 'NONE':
            __M_writer('      <table class="detstab" style="border-top-style:solid;border-color:rgb(189, 189, 189);border-width:1px;">\r\n         <tr>\r\n')
            if sellsOpiod:
                __M_writer('            <td class="botinfo">\r\n                 <p class="head">Opiates Prescribed</p>\r\n                 <table width="100%" style="text-align:left;line-height: 1rem;">\r\n                    <tr class="darkgreyback">\r\n                       <th class="rxName">\r\n                          Name\r\n                       </th>\r\n                       <th>\r\n                          Total Prescriptions\r\n                       </th>\r\n                       <th>\r\n                          Specialty Average\r\n                       </th>\r\n                    </tr>\r\n                    <tr class="greyback">\r\n                       <td class="rxName">\r\n                          <a href="/portal/rxdetails/" class="link2">Acetaminophen Codeine</a>\r\n                       </td>\r\n                       <td>\r\n                          ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.acetaminophen_codeine))
                __M_writer('\r\n                       </td>\r\n')
                if opiates.dif_acetmin_p > 0: 
                    __M_writer('                       <td class="rxOver">\r\n                           ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_acetmin_p))
                    __M_writer('% &#x1f845;\r\n                       </td>\r\n')
                elif opiates.dif_acetmin_p == 0: 
                    __M_writer('                       <td class="rxOn">\r\n                           &mdash;\r\n                       </td>\r\n')
                else:
                    __M_writer('                       <td class="rxUnder">\r\n                           ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_acetmin_p))
                    __M_writer('% \t &#x1f847;\r\n                       </td>\r\n')
                __M_writer('                    </tr>\r\n                    <tr>\r\n                        <td class="rxName">\r\n                           <a href="/portal/rxdetails/" class="link2">Fentanyl</a>\r\n                        </td>\r\n                        <td>\r\n                           ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.fentanyl))
                __M_writer('\r\n                        </td>\r\n')
                if opiates.dif_fenty_p > 0: 
                    __M_writer('                        <td class="rxOver">\r\n                            ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_fenty_p))
                    __M_writer('% &#8593;\r\n                        </td>\r\n')
                elif opiates.dif_fenty_p == 0: 
                    __M_writer('                        <td class="rxOn">\r\n                            &mdash;\r\n                        </td>\r\n')
                else:
                    __M_writer('                        <td class="rxUnder">\r\n                            ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_fenty_p))
                    __M_writer('% &#x1f847;\r\n                        </td>\r\n')
                __M_writer('                     </tr>\r\n                     <tr class="greyback">\r\n                           <td class="rxName">\r\n                              <a href="/portal/rxdetails/" class="link2">Hydrocodone Acetaminophen</a>\r\n                           </td>\r\n                           <td>\r\n                              ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.hydrocodone_acetaminophen))
                __M_writer('\r\n                           </td>\r\n')
                if opiates.dif_hydro_aceta_p > 0: 
                    __M_writer('                           <td class="rxOver">\r\n                               ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_hydro_aceta_p))
                    __M_writer('%  &#x1f845;\r\n                           </td>\r\n')
                elif opiates.dif_hydro_aceta_p == 0: 
                    __M_writer('                           <td class="rxOn">\r\n                              &mdash;\r\n                           </td>\r\n')
                else:
                    __M_writer('                           <td class="rxUnder">\r\n                               ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_hydro_aceta_p))
                    __M_writer('% \t &#x1f847;\r\n                           </td>\r\n')
                __M_writer('                        </tr>\r\n                        <tr>\r\n                              <td class="rxName">\r\n                                 <a href="/portal/rxdetails/" class="link2">Hydromorphone HCL</a>\r\n                              </td>\r\n                              <td>\r\n                                 ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.hydromorphone_hcl))
                __M_writer('\r\n                              </td>\r\n')
                if opiates.dif_hydromorphone_p > 0: 
                    __M_writer('                              <td class="rxOver">\r\n                                  ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_hydromorphone_p))
                    __M_writer('%  &#x1f845;\r\n                              </td>\r\n')
                elif opiates.dif_hydromorphone_p == 0: 
                    __M_writer('                              <td class="rxOn">\r\n                                  &mdash;\r\n                              </td>\r\n')
                else:
                    __M_writer('                              <td class="rxUnder">\r\n                                  ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_hydromorphone_p))
                    __M_writer('% &#x1f847;\r\n                              </td>\r\n')
                __M_writer('                           </tr>\r\n                           <tr class="greyback">\r\n                                 <td class="rxName">\r\n                                    <a href="/portal/rxdetails/" class="link2">Methadone HCL</a>\r\n                                 </td>\r\n                                 <td>\r\n                                    ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.methadone_hcl))
                __M_writer('\r\n                                 </td>\r\n')
                if opiates.dif_methadone_p > 0: 
                    __M_writer('                                 <td class="rxOver">\r\n                                     ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_methadone_p))
                    __M_writer('% &#x1f845;\r\n                                 </td>\r\n')
                elif opiates.dif_methadone_p == 0: 
                    __M_writer('                                 <td class="rxOn">\r\n                                     &mdash;\r\n                                 </td>\r\n')
                else:
                    __M_writer('                                 <td class="rxUnder">\r\n                                     ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_methadone_p))
                    __M_writer('% &#x1f847;\r\n                                 </td>\r\n')
                __M_writer('                              </tr>\r\n                              <tr>\r\n                                    <td class="rxName">\r\n                                       <a href="/portal/rxdetails/" class="link2">Morphine Sulfate</a>\r\n                                    </td>\r\n                                    <td>\r\n                                       ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.morphine_sulfate))
                __M_writer('\r\n                                    </td>\r\n')
                if opiates.dif_morphine_p > 0: 
                    __M_writer('                                    <td class="rxOver">\r\n                                        ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_morphine_p))
                    __M_writer('% &#x1f845;\r\n                                    </td>\r\n')
                elif opiates.dif_morphine_p == 0: 
                    __M_writer('                                    <td class="rxOn">\r\n                                        &mdash;\r\n                                    </td>\r\n')
                else:
                    __M_writer('                                    <td class="rxUnder">\r\n                                        ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_morphine_p))
                    __M_writer('% &#x1f847;\r\n                                    </td>\r\n')
                __M_writer('                                 </tr>\r\n                                 <tr class="greyback">\r\n                       <td class="rxName">\r\n                          <a href="/portal/rxdetails/" class="link2">Morphine Extended Release</a>\r\n                       </td>\r\n                       <td>\r\n                          ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.morphine_sulfate_er))
                __M_writer('\r\n                       </td>\r\n')
                if opiates.dif_morphine_ext_p > 0: 
                    __M_writer('                       <td class="rxOver">\r\n                           ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_morphine_ext_p))
                    __M_writer('% &#x1f845;\r\n                       </td>\r\n')
                elif opiates.dif_morphine_ext_p == 0: 
                    __M_writer('                       <td class="rxOn">\r\n                           &mdash;\r\n                       </td>\r\n')
                else:
                    __M_writer('                       <td class="rxUnder">\r\n                           ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_morphine_ext_p))
                    __M_writer('% &#x1f847;\r\n                       </td>\r\n')
                __M_writer('                    </tr>\r\n                    <tr>\r\n                       <td class="rxName">\r\n                          <a href="/portal/rxdetails/" class="link2">Oxycodone Acetaminophen</a>\r\n                       </td>\r\n                       <td>\r\n                          ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.oxycodone_acetaminophen))
                __M_writer('\r\n                       </td>\r\n')
                if opiates.dif_oxy_aceta_p > 0: 
                    __M_writer('                       <td class="rxOver">\r\n                           ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_oxy_aceta_p))
                    __M_writer('% &#x1f845;\r\n                       </td>\r\n')
                elif opiates.dif_oxy_aceta_p == 0: 
                    __M_writer('                       <td class="rxOn">\r\n                           &mdash;\r\n                       </td>\r\n')
                else:
                    __M_writer('                       <td class="rxUnder">\r\n                           ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_oxy_aceta_p))
                    __M_writer('% &#x1f847;\r\n                       </td>\r\n')
                __M_writer('                    </tr>\r\n                    <tr class="greyback">\r\n                        <td class="rxName">\r\n                           <a href="/portal/rxdetails/" class="link2">Oxycodone HCL</a>\r\n                        </td>\r\n                        <td>\r\n                           ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.oxycodone_hcl))
                __M_writer('\r\n                        </td>\r\n')
                if opiates.dif_oxy_hcl_p > 0: 
                    __M_writer('                        <td class="rxOver">\r\n                            ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_oxy_hcl_p))
                    __M_writer('% &#x1f845;\r\n                        </td>\r\n')
                elif opiates.dif_oxy_hcl_p == 0: 
                    __M_writer('                        <td class="rxOn">\r\n                            &mdash;\r\n                        </td>\r\n')
                else:
                    __M_writer('                        <td class="rxUnder">\r\n                            ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_oxy_hcl_p))
                    __M_writer('% &#x1f847;\r\n                        </td>\r\n')
                __M_writer('                     </tr>\r\n                     <tr>\r\n                           <td class="rxName">\r\n                              <a href="/portal/rxdetails/" class="link2">Oxycontin</a>\r\n                           </td>\r\n                           <td>\r\n                              ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.oxycontin))
                __M_writer('\r\n                           </td>\r\n')
                if opiates.dif_oxycotin_p > 0: 
                    __M_writer('                           <td class="rxOver">\r\n                               ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_oxycotin_p))
                    __M_writer('% &#x1f845;\r\n                           </td>\r\n')
                elif opiates.dif_oxycotin_p == 0: 
                    __M_writer('                           <td class="rxOn">\r\n                               &mdash;\r\n                           </td>\r\n')
                else:
                    __M_writer('                           <td class="rxUnder">\r\n                               ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_oxycotin_p))
                    __M_writer('% &#x1f847;\r\n                           </td>\r\n')
                __M_writer('                        </tr>\r\n                     <tr class="greyback">\r\n                           <td class="rxName">\r\n                              <a href="/portal/rxdetails/" class="link2">Tramadol HCL</a>\r\n                           </td>\r\n                           <td>\r\n                              ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.tramadol_hcl))
                __M_writer('\r\n                           </td>\r\n')
                if opiates.dif_tramadol_p > 0: 
                    __M_writer('                           <td class="rxOver">\r\n                               ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_tramadol_p))
                    __M_writer('% &#x1f845;\r\n                           </td>\r\n')
                elif opiates.dif_tramadol_p == 0: 
                    __M_writer('                           <td class="rxOn">\r\n                               &mdash;\r\n                           </td>\r\n')
                else:
                    __M_writer('                           <td class="rxUnder">\r\n                               ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(opiates.dif_tramadol_p))
                    __M_writer('% &#x1f847;\r\n                           </td>\r\n')
                __M_writer('                        </tr>\r\n                 </table>\r\n\r\n            </td>\r\n')
            else:
                __M_writer('            <td class="botinfo">\r\n                  <p class="head">Likelihood of future<br> opiod-prescriptions</p>\r\n')
                if risk == 'High':
                    __M_writer('                  <p class="redRisk" style="font-size:50px;">')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(risk))
                    __M_writer('</p>\r\n')
                elif risk == 'Medium':
                    __M_writer('                  <p class="yellow" style="font-size:50px;">')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(risk))
                    __M_writer('</p>\r\n')
                elif risk == 'Low':
                    __M_writer('                  <p class="green" style="font-size:50px;">')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(risk))
                    __M_writer('</p>\r\n')
                else:
                    __M_writer('                  <p class="" style="font-size:50px;">')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(risk))
                    __M_writer('</p>\r\n')
                __M_writer('             </td>\r\n')
            __M_writer('            <td style="width:0px;border-right-style:solid;border-color:rgb(189, 189, 189);border-width:1px; padding:10px;"></td>\r\n            <td class="botinfo">\r\n                  <p class="head">Similar Prescribers</p>\r\n                  <table width="100%" style="text-align:left;line-height: 1rem;">\r\n                        \r\n')
            for human in relatives:
                __M_writer('                  \r\n                  <tr class="botbord">\r\n                        <td class="rxName">\r\n                              <a href="/portal/details/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(human.doctorid))
                __M_writer('/" class="link2" ><p style="font-size:20px;">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(human.fname))
                __M_writer(' ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(human.lname))
                __M_writer('</p></a>\r\n                        </td>\r\n                        <td style="line-height:20px">\r\n                           ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(human.specialty))
                __M_writer('\r\n                        </td>\r\n                     </tr>\r\n                  \r\n')
            __M_writer('                     </table>\r\n            </td>\r\n         </tr>\r\n      </table>\r\n')
        __M_writer('         \r\n         \r\n   </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/intexsite/portal/templates/prescriberdetails.html", "uri": "prescriberdetails.html", "source_encoding": "utf-8", "line_map": {"29": 0, "57": 1, "62": 3, "67": 7, "72": 330, "82": 3, "88": 3, "94": 5, "100": 5, "106": 9, "127": 9, "128": 14, "129": 14, "130": 17, "131": 17, "132": 17, "133": 17, "134": 18, "135": 18, "136": 18, "137": 18, "138": 19, "139": 19, "140": 19, "141": 19, "142": 20, "143": 21, "144": 21, "145": 21, "146": 21, "147": 21, "148": 21, "149": 21, "150": 23, "151": 27, "152": 27, "153": 30, "154": 30, "155": 33, "156": 33, "157": 34, "158": 34, "159": 39, "160": 40, "161": 42, "162": 43, "163": 62, "164": 62, "165": 64, "166": 65, "167": 66, "168": 66, "169": 68, "170": 69, "171": 72, "172": 73, "173": 74, "174": 74, "175": 77, "176": 83, "177": 83, "178": 85, "179": 86, "180": 87, "181": 87, "182": 89, "183": 90, "184": 93, "185": 94, "186": 95, "187": 95, "188": 98, "189": 104, "190": 104, "191": 106, "192": 107, "193": 108, "194": 108, "195": 110, "196": 111, "197": 114, "198": 115, "199": 116, "200": 116, "201": 119, "202": 125, "203": 125, "204": 127, "205": 128, "206": 129, "207": 129, "208": 131, "209": 132, "210": 135, "211": 136, "212": 137, "213": 137, "214": 140, "215": 146, "216": 146, "217": 148, "218": 149, "219": 150, "220": 150, "221": 152, "222": 153, "223": 156, "224": 157, "225": 158, "226": 158, "227": 161, "228": 167, "229": 167, "230": 169, "231": 170, "232": 171, "233": 171, "234": 173, "235": 174, "236": 177, "237": 178, "238": 179, "239": 179, "240": 182, "241": 188, "242": 188, "243": 190, "244": 191, "245": 192, "246": 192, "247": 194, "248": 195, "249": 198, "250": 199, "251": 200, "252": 200, "253": 203, "254": 209, "255": 209, "256": 211, "257": 212, "258": 213, "259": 213, "260": 215, "261": 216, "262": 219, "263": 220, "264": 221, "265": 221, "266": 224, "267": 230, "268": 230, "269": 232, "270": 233, "271": 234, "272": 234, "273": 236, "274": 237, "275": 240, "276": 241, "277": 242, "278": 242, "279": 245, "280": 251, "281": 251, "282": 253, "283": 254, "284": 255, "285": 255, "286": 257, "287": 258, "288": 261, "289": 262, "290": 263, "291": 263, "292": 266, "293": 272, "294": 272, "295": 274, "296": 275, "297": 276, "298": 276, "299": 278, "300": 279, "301": 282, "302": 283, "303": 284, "304": 284, "305": 287, "306": 291, "307": 292, "308": 294, "309": 295, "310": 295, "311": 295, "312": 296, "313": 297, "314": 297, "315": 297, "316": 298, "317": 299, "318": 299, "319": 299, "320": 300, "321": 301, "322": 301, "323": 301, "324": 303, "325": 305, "326": 310, "327": 311, "328": 314, "329": 314, "330": 314, "331": 314, "332": 314, "333": 314, "334": 317, "335": 317, "336": 322, "337": 327, "343": 332, "349": 332, "355": 349}}
__M_END_METADATA
"""
