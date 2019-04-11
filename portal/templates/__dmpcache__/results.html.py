# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555023574.2866788
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/portal/templates/results.html'
_template_uri = 'results.html'
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
        providers = context.get('providers', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        prescripts = context.get('prescripts', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        hasprov = context.get('hasprov', UNDEFINED)
        hasdrug = context.get('hasdrug', UNDEFINED)
        self = context.get('self', UNDEFINED)
        num = context.get('num', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n')
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
        __M_writer('&mdash; Search')
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
        providers = context.get('providers', UNDEFINED)
        prescripts = context.get('prescripts', UNDEFINED)
        request = context.get('request', UNDEFINED)
        hasprov = context.get('hasprov', UNDEFINED)
        hasdrug = context.get('hasdrug', UNDEFINED)
        self = context.get('self', UNDEFINED)
        num = context.get('num', UNDEFINED)
        def site_content():
            return render_site_content(context)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="content">\r\n    <p class="portaltitle">Results</p>\r\n    <hr>\r\n    <table style="width:100%;">\r\n        <tr>\r\n')
        if hasprov:
            __M_writer('                <td  class="bigtab">\r\n                    <p class="tabhead">Providers</p>\r\n                    <table class="provtab">\r\n                    <th>\r\n')
            if request.user.has_perm('account.search'):
                __M_writer('                            <p>Name</p>\r\n')
            elif request.user.has_perm('account.safesearch'):
                __M_writer('                            <p>Doctor ID</p>\r\n')
            __M_writer('                        \r\n                    </th>\r\n                    <th>\r\n                        <p>Gender</p>\r\n                    </th>\r\n                    <th>\r\n                        <p>Location</p>\r\n                    </th>\r\n                    <th>\r\n                        <p>Credentials</p>\r\n                    </th>\r\n                    <th>\r\n                        <p>Specialty</p>\r\n                    </th>\r\n')
            for item in providers:
                __M_writer('                    <tr>\r\n                        <td>\r\n')
                if request.user.has_perm('account.search'):
                    __M_writer('                            <a href="/portal/details/')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.doctorid))
                    __M_writer('" class="link2"><p>')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.fname))
                    __M_writer('  ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.lname))
                    __M_writer('</p></a>\r\n')
                elif request.user.has_perm('account.safesearch'):
                    __M_writer('                            <a href="/portal/details/')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.doctorid))
                    __M_writer('" class="link2"><p>')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.doctorid))
                    __M_writer('</p></a>\r\n')
                __M_writer('                        </td>        \r\n                        <td>\r\n                            <p>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.gender))
                __M_writer('</p>\r\n                        </td>        \r\n                        <td>\r\n                            <p>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.state))
                __M_writer('</p>\r\n                        </td>\r\n                        <td>\r\n                            <p>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.credentials))
                __M_writer('</p>\r\n                        </td> \r\n                        <td>\r\n                            <p>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.specialty))
                __M_writer('</p>\r\n                        </td>         \r\n                    </tr>\r\n                    \r\n')
            __M_writer('                </table>\r\n')
            if len(providers) == 0:
                __M_writer('                    <p>No Results</p>\r\n')
            __M_writer('                </td>\r\n')
        if hasprov and hasdrug:
            __M_writer('                <td style="border-left-color:rgb(218, 218, 218);border-left-style:solid;border-width:1px; width:40px"></td>\r\n')
        if hasdrug:
            __M_writer('                <td  class="bigtab">\r\n                    <p class="tabhead">Prescriptions</p>\r\n                    <table class="provtab">\r\n                    <th>\r\n                        <p>Name</p>\r\n                    </th>\r\n                    <th>\r\n                        <p>Type</p>\r\n                    </th>\r\n')
            for item in prescripts:
                __M_writer('                    <tr>\r\n                        <td>\r\n                                <a href="/portal/rxdetails/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.id))
                __M_writer('" class="link2"><p>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.drugName))
                __M_writer('</p></a>\r\n                        </td>        \r\n                        <td>\r\n                            <p>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)('Opioid' if item.isOpioid else 'Non-Opioid'))
                __M_writer('</p>\r\n                        </td>        \r\n')
            __M_writer('                </table>\r\n')
            if len(prescripts) == 0:
                __M_writer('                    <p>No Results</p>\r\n')
            __M_writer('            </td>        \r\n')
        __M_writer('\r\n                \r\n        </tr>\r\n    </table>\r\n    <table class="nextprev" width=100%>\r\n                <td width=50%>       \r\n')
        if num > 20:
            __M_writer('                    <p style="text-align:center;font-family: century gothic">Showing top 20 out of ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(num))
            __M_writer(' results. Refine your search <a class="link2" href="/portal/search/">here.</a></p>\r\n')
        __M_writer('                </td>\r\n            </tr>\r\n        </table>\r\n    <a href="/portal/search/" style="color:#273B7A; font-family: \'Century Gothic\';font-weight: bold;">Back to Search</a>\r\n    \r\n</div>\r\n')
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
{"filename": "C:/Users/Isaac/intexsite/portal/templates/results.html", "uri": "results.html", "source_encoding": "utf-8", "line_map": {"29": 0, "50": 1, "55": 3, "60": 6, "65": 112, "75": 3, "81": 3, "87": 4, "93": 4, "99": 8, "113": 8, "114": 15, "115": 16, "116": 20, "117": 21, "118": 22, "119": 23, "120": 25, "121": 39, "122": 40, "123": 42, "124": 43, "125": 43, "126": 43, "127": 43, "128": 43, "129": 43, "130": 43, "131": 44, "132": 45, "133": 45, "134": 45, "135": 45, "136": 45, "137": 47, "138": 49, "139": 49, "140": 52, "141": 52, "142": 55, "143": 55, "144": 58, "145": 58, "146": 63, "147": 64, "148": 65, "149": 67, "150": 69, "151": 70, "152": 72, "153": 73, "154": 82, "155": 83, "156": 85, "157": 85, "158": 85, "159": 85, "160": 88, "161": 88, "162": 91, "163": 92, "164": 93, "165": 95, "166": 97, "167": 103, "168": 104, "169": 104, "170": 104, "171": 106, "177": 114, "183": 114, "189": 183}}
__M_END_METADATA
"""
