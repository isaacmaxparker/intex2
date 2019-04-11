# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555023076.2452633
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
        opiates = context.get('opiates', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        risk = context.get('risk', UNDEFINED)
        relatives = context.get('relatives', UNDEFINED)
        specialty = context.get('specialty', UNDEFINED)
        self = context.get('self', UNDEFINED)
        sellsOpiod = context.get('sellsOpiod', UNDEFINED)
        state = context.get('state', UNDEFINED)
        deaths = context.get('deaths', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        statename = context.get('statename', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        gender = context.get('gender', UNDEFINED)
        fullname = context.get('fullname', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
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
        opiates = context.get('opiates', UNDEFINED)
        sellsOpiod = context.get('sellsOpiod', UNDEFINED)
        state = context.get('state', UNDEFINED)
        deaths = context.get('deaths', UNDEFINED)
        def site_content():
            return render_site_content(context)
        statename = context.get('statename', UNDEFINED)
        request = context.get('request', UNDEFINED)
        risk = context.get('risk', UNDEFINED)
        gender = context.get('gender', UNDEFINED)
        fullname = context.get('fullname', UNDEFINED)
        relatives = context.get('relatives', UNDEFINED)
        specialty = context.get('specialty', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n   <div class="content">\r\n      <table class="detstab">\r\n         <tr>\r\n            <td>\r\n                  <img src="/static/homepage/media/UserImages/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)('Male' if gender == 'M' else 'Female'))
        __M_writer('.png">\r\n            </td>\r\n            <td class="bio">\r\n                  <p class="name">')
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
        __M_writer('</span></p>\r\n                  \r\n            </td>\r\n            <td style="width:0px;border-right-style:solid;border-color:rgb(189, 189, 189);border-width:1px; padding:10px;"></td>\r\n            <td style="vertical-align:middle; padding-left:40px;">\r\n               <p class="stat" style="font-size:60px;line-height: 30px;">\r\n                  ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(deaths))
        __M_writer('\r\n               </p>\r\n               <p style="font-size:20px;">\r\n                  opiod-related <br>deaths in <b>')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(state))
        __M_writer('</b>\r\n               </p>\r\n            </td>\r\n         </tr>\r\n      </table>\r\n')
        if request.user.has_perm('account.search'):
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
{"filename": "C:/Users/Isaac/intexsite/portal/templates/prescriberdetails.html", "uri": "prescriberdetails.html", "source_encoding": "utf-8", "line_map": {"29": 0, "54": 1, "59": 3, "64": 7, "69": 324, "79": 3, "85": 3, "91": 5, "97": 5, "103": 9, "121": 9, "122": 14, "123": 14, "124": 17, "125": 17, "126": 17, "127": 17, "128": 18, "129": 18, "130": 18, "131": 18, "132": 19, "133": 19, "134": 19, "135": 19, "136": 25, "137": 25, "138": 28, "139": 28, "140": 33, "141": 34, "142": 36, "143": 37, "144": 56, "145": 56, "146": 58, "147": 59, "148": 60, "149": 60, "150": 62, "151": 63, "152": 66, "153": 67, "154": 68, "155": 68, "156": 71, "157": 77, "158": 77, "159": 79, "160": 80, "161": 81, "162": 81, "163": 83, "164": 84, "165": 87, "166": 88, "167": 89, "168": 89, "169": 92, "170": 98, "171": 98, "172": 100, "173": 101, "174": 102, "175": 102, "176": 104, "177": 105, "178": 108, "179": 109, "180": 110, "181": 110, "182": 113, "183": 119, "184": 119, "185": 121, "186": 122, "187": 123, "188": 123, "189": 125, "190": 126, "191": 129, "192": 130, "193": 131, "194": 131, "195": 134, "196": 140, "197": 140, "198": 142, "199": 143, "200": 144, "201": 144, "202": 146, "203": 147, "204": 150, "205": 151, "206": 152, "207": 152, "208": 155, "209": 161, "210": 161, "211": 163, "212": 164, "213": 165, "214": 165, "215": 167, "216": 168, "217": 171, "218": 172, "219": 173, "220": 173, "221": 176, "222": 182, "223": 182, "224": 184, "225": 185, "226": 186, "227": 186, "228": 188, "229": 189, "230": 192, "231": 193, "232": 194, "233": 194, "234": 197, "235": 203, "236": 203, "237": 205, "238": 206, "239": 207, "240": 207, "241": 209, "242": 210, "243": 213, "244": 214, "245": 215, "246": 215, "247": 218, "248": 224, "249": 224, "250": 226, "251": 227, "252": 228, "253": 228, "254": 230, "255": 231, "256": 234, "257": 235, "258": 236, "259": 236, "260": 239, "261": 245, "262": 245, "263": 247, "264": 248, "265": 249, "266": 249, "267": 251, "268": 252, "269": 255, "270": 256, "271": 257, "272": 257, "273": 260, "274": 266, "275": 266, "276": 268, "277": 269, "278": 270, "279": 270, "280": 272, "281": 273, "282": 276, "283": 277, "284": 278, "285": 278, "286": 281, "287": 285, "288": 286, "289": 288, "290": 289, "291": 289, "292": 289, "293": 290, "294": 291, "295": 291, "296": 291, "297": 292, "298": 293, "299": 293, "300": 293, "301": 294, "302": 295, "303": 295, "304": 295, "305": 297, "306": 299, "307": 304, "308": 305, "309": 308, "310": 308, "311": 308, "312": 308, "313": 308, "314": 308, "315": 311, "316": 311, "317": 316, "318": 321, "324": 326, "330": 326, "336": 330}}
__M_END_METADATA
"""
