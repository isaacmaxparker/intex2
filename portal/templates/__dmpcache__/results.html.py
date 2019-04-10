# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554857565.9895978
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
        def page_title():
            return render_page_title(context._locals(__M_locals))
        hasdrug = context.get('hasdrug', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        hasprov = context.get('hasprov', UNDEFINED)
        prescripts = context.get('prescripts', UNDEFINED)
        providers = context.get('providers', UNDEFINED)
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
        hasdrug = context.get('hasdrug', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_content():
            return render_site_content(context)
        hasprov = context.get('hasprov', UNDEFINED)
        prescripts = context.get('prescripts', UNDEFINED)
        providers = context.get('providers', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="content">\r\n    <p class="portaltitle">Results</p>\r\n    <hr>\r\n    <table style="width:100%;">\r\n        <tr>\r\n')
        if hasprov:
            __M_writer('                <td  class="bigtab">\r\n                    <p class="tabhead">Providers</p>\r\n                    <table class="provtab">\r\n                    <th>\r\n                        <p>Name</p>\r\n                    </th>\r\n                    <th>\r\n                        <p>Gender</p>\r\n                    </th>\r\n                    <th>\r\n                        <p>Location</p>\r\n                    </th>\r\n                    <th>\r\n                        <p>Certifications</p>\r\n                    </th>\r\n                    <th>\r\n                        <p>Specialty</p>\r\n                    </th>\r\n')
            for item in providers:
                __M_writer('                    <tr>\r\n                        <td>\r\n                            <a href="/portal/details/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.id))
                __M_writer('" class="link2"><p>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.first_name))
                __M_writer('  ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.last_name))
                __M_writer('</p></a>\r\n                        </td>        \r\n                        <td>\r\n                            <p>M</p>\r\n                        </td>        \r\n                        <td>\r\n                            <p>UT</p>\r\n                        </td>\r\n                        <td>\r\n                            <p>DDS</p>\r\n                        </td> \r\n                        <td>\r\n                            <p>Dentist</p>\r\n                        </td>         \r\n                    </tr>\r\n                    \r\n')
            __M_writer('                </table>\r\n')
            if len(providers) == 0:
                __M_writer('                    <p>No Results</p>\r\n')
            __M_writer('                </td>\r\n')
        if hasprov and hasdrug:
            __M_writer('                <td style="border-left-color:rgb(218, 218, 218);border-left-style:solid;border-width:1px; width:40px"></td>\r\n')
        if hasdrug:
            __M_writer('                <td  class="bigtab">\r\n                    <p class="tabhead">Prescriptions</p>\r\n                    <table class="provtab">\r\n                    <th>\r\n                        <p>Name</p>\r\n                    </th>\r\n                    <th>\r\n                        <p>Type</p>\r\n                    </th>\r\n')
            for item in prescripts:
                __M_writer('                    <tr>\r\n                        <td>\r\n                            <p>')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.username))
                __M_writer('</p>\r\n                        </td>        \r\n                        <td>\r\n                            <p>Opiod</p>\r\n                        </td>        \r\n')
            __M_writer('                </table>\r\n')
            if len(prescripts) == 0:
                __M_writer('                    <p>No Results</p>\r\n')
            __M_writer('            </td>        \r\n')
        __M_writer('\r\n                \r\n        </tr>\r\n    </table>\r\n    <a href="/portal/search/" style="color:#273B7A; font-family: \'Century Gothic\';font-weight: bold;">Back to Search</a>\r\n</div>\r\n')
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
{"filename": "C:/Users/Isaac/intexsite/portal/templates/results.html", "uri": "results.html", "source_encoding": "utf-8", "line_map": {"29": 0, "48": 1, "53": 3, "58": 6, "63": 94, "73": 3, "79": 3, "85": 4, "91": 4, "97": 8, "109": 8, "110": 15, "111": 16, "112": 34, "113": 35, "114": 37, "115": 37, "116": 37, "117": 37, "118": 37, "119": 37, "120": 54, "121": 55, "122": 56, "123": 58, "124": 60, "125": 61, "126": 63, "127": 64, "128": 73, "129": 74, "130": 76, "131": 76, "132": 82, "133": 83, "134": 84, "135": 86, "136": 88, "142": 96, "148": 96, "154": 148}}
__M_END_METADATA
"""
