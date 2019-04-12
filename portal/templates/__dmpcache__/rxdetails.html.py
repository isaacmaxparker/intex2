# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555049468.3588023
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/portal/templates/rxdetails.html'
_template_uri = 'rxdetails.html'
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
        rxImage = context.get('rxImage', UNDEFINED)
        request = context.get('request', UNDEFINED)
        isOpiod = context.get('isOpiod', UNDEFINED)
        onlyguys = context.get('onlyguys', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
        sellsOpiod = context.get('sellsOpiod', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        rxPercent = context.get('rxPercent', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        topguys = context.get('topguys', UNDEFINED)
        rxName = context.get('rxName', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n\r\n\r\n\r\n\r\n')
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
        rxImage = context.get('rxImage', UNDEFINED)
        request = context.get('request', UNDEFINED)
        isOpiod = context.get('isOpiod', UNDEFINED)
        onlyguys = context.get('onlyguys', UNDEFINED)
        len = context.get('len', UNDEFINED)
        sellsOpiod = context.get('sellsOpiod', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_content():
            return render_site_content(context)
        rxPercent = context.get('rxPercent', UNDEFINED)
        topguys = context.get('topguys', UNDEFINED)
        rxName = context.get('rxName', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n   <div class="content">\r\n')
        if request.user.has_perm('account.search'):
            __M_writer('            <table class="detstab" style="width:100%;">\r\n                  <tr style="border-bottom-style:solid;border-color:rgb(189, 189, 189);border-width:1px;">')
            __M_writer('                     <td>\r\n                           <img src="/static/homepage/media/DrugImages/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(rxImage))
            __M_writer('.png">\r\n                     </td>\r\n                     <td class="bio" style="padding-left:10px;">\r\n                           <p class="name" style="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)('font-size:46px;' if len(rxName) >= 26 else ''))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(rxName))
            __M_writer('</p>\r\n                           <p class="info"><span class="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)('red' if sellsOpiod else ''))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)('Opioid' if isOpiod else 'Non-Opiate' ))
            __M_writer('</span></p>     \r\n                     </td>\r\n                  </tr>\r\n               </table>  \r\n            <table style="width:100%;max-width:100%;display: inline-block;">\r\n            <tr style="width:100%;">\r\n')
            if rxPercent != '0.00%':
                __M_writer('                  <td style="vertical-align:middle; text-align: center; margin-left:20px;">\r\n                        <p class="stat" style="font-size:90px;line-height: 90px; display: inline;">\r\n                                          ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(rxPercent))
                __M_writer('\r\n                                       </p>\r\n                                    <p style="font-size:20px; padding-left:20px;">\r\n                                          of doctors overprescribe <br><em>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(rxName))
                __M_writer('</em>\r\n                                    </p>  \r\n                  </td>\r\n                  <td style="width:0px;border-right-style:solid;border-color:rgb(189, 189, 189);border-width:1px; padding:10px;"></td>\r\n')
            if isOpiod:
                __M_writer('               <td class="botinfo" style="padding-left:20px;text-align: center;">\r\n                  <p class="head">Top Overprescribers</p>\r\n')
                if topguys != '':
                    for guy in topguys:
                        __M_writer('                  <a href="/portal/details/')
                        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(guy.doctorid))
                        __M_writer('/" class="link2" ><p style="font-size:20px;">')
                        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(guy.fname))
                        __M_writer(' ')
                        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(guy.lname))
                        __M_writer('</p></a>\r\n')
                else:
                    __M_writer('                  <p class="homeparg">Not Enough Data</p>\r\n')
                __M_writer('               </td>\r\n               <td style="width:0px;border-right-style:solid;border-color:rgb(189, 189, 189);border-width:1px; padding:10px;"></td>\r\n               <td class="botinfo" style="padding-left:20px;text-align:center;">\r\n                     <p class="head">Sole Prescribers</p>\r\n')
                if topguys != '':
                    for guy in onlyguys:
                        __M_writer('                     <a href="/portal/details/')
                        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(guy.doctorid))
                        __M_writer('/" class="link2" ><p style="font-size:20px;">')
                        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(guy.fname))
                        __M_writer(' ')
                        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(guy.lname))
                        __M_writer('</p></a>\r\n')
                else:
                    __M_writer('                  <p class="homeparg">Not Enough Data</p>\r\n')
                __M_writer('               </td>\r\n')
            __M_writer('            </tr>\r\n         </table>   \r\n')
        else:
            __M_writer('            <div class="detstab" style="width:100%;">\r\n                     <div style="display:inline-block; width:100px;">\r\n                           <img src="/static/homepage/media/DrugImages/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(rxImage))
            __M_writer('.png">\r\n                     </div>\r\n                     <div class="bio" style="display: inline-block;">\r\n')
            if len(rxName) <= 20:
                __M_writer('                        <p class="name" style="font-size:46px;">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(rxName))
                __M_writer('</p>\r\n')
            else:
                if len(rxName) <= 25:
                    __M_writer('                           <p class="name" style="font-size:36px;">')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(rxName))
                    __M_writer('</p>\r\n')
                else:
                    __M_writer('                           <p class="name" style="font-size:26px;">')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(rxName))
                    __M_writer('</p>\r\n')
            __M_writer('                           \r\n                           <p class="info"><span class="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)('red' if sellsOpiod else ''))
            __M_writer('">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)('Opiate' if isOpiod else 'Non-Opiate' ))
            __M_writer('</span></p>     \r\n                     </div>\r\n                     <div class="bio percent" style="display:inline-block">\r\n                           <p class="stat" style="font-size:90px;line-height: 90px;">\r\n                                 ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(rxPercent))
            __M_writer('\r\n                           </p>\r\n                           <p style="font-size:16px;">\r\n                                 of doctors overprescribe <br><em>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(rxName))
            __M_writer('</em>\r\n                           </p>  \r\n                     </div>\r\n            </div>  \r\n')
        __M_writer('               \r\n   </div>\r\n')
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
{"filename": "C:/Users/Isaac/intexsite/portal/templates/rxdetails.html", "uri": "rxdetails.html", "source_encoding": "utf-8", "line_map": {"29": 0, "52": 1, "53": 8, "58": 10, "63": 14, "68": 98, "78": 10, "84": 10, "90": 12, "96": 12, "102": 16, "118": 16, "119": 18, "120": 19, "121": 21, "122": 22, "123": 22, "124": 25, "125": 25, "126": 25, "127": 25, "128": 26, "129": 26, "130": 26, "131": 26, "132": 32, "133": 33, "134": 35, "135": 35, "136": 38, "137": 38, "138": 43, "139": 44, "140": 46, "141": 47, "142": 48, "143": 48, "144": 48, "145": 48, "146": 48, "147": 48, "148": 48, "149": 50, "150": 51, "151": 53, "152": 57, "153": 58, "154": 59, "155": 59, "156": 59, "157": 59, "158": 59, "159": 59, "160": 59, "161": 61, "162": 62, "163": 64, "164": 66, "165": 68, "166": 69, "167": 71, "168": 71, "169": 74, "170": 75, "171": 75, "172": 75, "173": 76, "174": 77, "175": 78, "176": 78, "177": 78, "178": 79, "179": 80, "180": 80, "181": 80, "182": 83, "183": 84, "184": 84, "185": 84, "186": 84, "187": 88, "188": 88, "189": 91, "190": 91, "191": 96, "197": 100, "203": 100, "209": 203}}
__M_END_METADATA
"""
