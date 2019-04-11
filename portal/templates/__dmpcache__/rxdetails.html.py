# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554922665.008868
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
        self = context.get('self', UNDEFINED)
        sellsOpiod = context.get('sellsOpiod', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        isOpiod = context.get('isOpiod', UNDEFINED)
        rxPercent = context.get('rxPercent', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        rxName = context.get('rxName', UNDEFINED)
        request = context.get('request', UNDEFINED)
        rxImage = context.get('rxImage', UNDEFINED)
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
        self = context.get('self', UNDEFINED)
        sellsOpiod = context.get('sellsOpiod', UNDEFINED)
        isOpiod = context.get('isOpiod', UNDEFINED)
        rxPercent = context.get('rxPercent', UNDEFINED)
        len = context.get('len', UNDEFINED)
        def site_content():
            return render_site_content(context)
        rxName = context.get('rxName', UNDEFINED)
        request = context.get('request', UNDEFINED)
        rxImage = context.get('rxImage', UNDEFINED)
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
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)('Opiate' if isOpiod else 'Non-Opiate' ))
            __M_writer('</span></p>     \r\n                     </td>\r\n                  </tr>\r\n               </table>  \r\n            <table style="width:100%;max-width:100%;display: inline-block;">\r\n            <tr style="width:100%;">\r\n                  <td style="vertical-align:middle; text-align: center;">\r\n                        <p class="stat" style="font-size:90px;line-height: 90px; display: inline;">\r\n                                          ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(rxPercent))
            __M_writer('\r\n                                       </p>\r\n                                    <p style="font-size:20px; padding-left:20px;">\r\n                                          of doctors overprescribe <br><em>')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(rxName))
            __M_writer('</em>\r\n                                    </p>  \r\n                  </td>\r\n                  <td style="width:0px;border-right-style:solid;border-color:rgb(189, 189, 189);border-width:1px; padding:10px;"></td>\r\n')
            if isOpiod:
                __M_writer('               <td class="botinfo" style="padding-left:20px;text-align: center;">\r\n                  <p class="head">Top Overprescribers</p>\r\n                  <a href="/portal/details/1/" class="link2" ><p style="font-size:20px;">Other Dude</p></a>\r\n                  <a href="/portal/details/1/" class="link2" ><p style="font-size:20px;">Other Dude</p></a>\r\n                  <a href="/portal/details/1/" class="link2" ><p style="font-size:20px;">Other Dude</p></a>\r\n                  <a href="/portal/details/1/" class="link2" ><p style="font-size:20px;">Other Dude</p></a>\r\n                  <a href="/portal/details/1/" class="link2" ><p style="font-size:20px;">Other Dude</p></a>\r\n               </td>\r\n')
            else:
                __M_writer('               <td class="botinfo" style="padding-left:20px;text-align:left;">\r\n                     <p class="head">Related Prescriptions</p>\r\n                     <a href="/portal/details/1/" class="link2" ><p style="font-size:20px;">Other Drug</p></a>\r\n                     <a href="/portal/details/1/" class="link2 red" ><p style="font-size:20px;">Opiate</p></a>\r\n                     <a href="/portal/details/1/" class="link2 red" ><p style="font-size:20px;">Opiod</p></a>\r\n                     <a href="/portal/details/1/" class="link2" ><p style="font-size:20px;">Other Drug</p></a>\r\n               </td>\r\n')
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
{"filename": "C:/Users/Isaac/intexsite/portal/templates/rxdetails.html", "uri": "rxdetails.html", "source_encoding": "utf-8", "line_map": {"29": 0, "50": 1, "51": 8, "56": 10, "61": 14, "66": 91, "76": 10, "82": 10, "88": 12, "94": 12, "100": 16, "114": 16, "115": 18, "116": 19, "117": 21, "118": 22, "119": 22, "120": 25, "121": 25, "122": 25, "123": 25, "124": 26, "125": 26, "126": 26, "127": 26, "128": 34, "129": 34, "130": 37, "131": 37, "132": 41, "133": 42, "134": 50, "135": 51, "136": 59, "137": 61, "138": 62, "139": 64, "140": 64, "141": 67, "142": 68, "143": 68, "144": 68, "145": 69, "146": 70, "147": 71, "148": 71, "149": 71, "150": 72, "151": 73, "152": 73, "153": 73, "154": 76, "155": 77, "156": 77, "157": 77, "158": 77, "159": 81, "160": 81, "161": 84, "162": 84, "163": 89, "169": 93, "175": 93, "181": 175}}
__M_END_METADATA
"""
