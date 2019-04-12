# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555053520.9415965
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/portal/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'page_header_title', 'bodyclass', 'left_content', 'middleclass', 'right_content']


from catalog import models as cmod 

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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def middleclass():
            return render_middleclass(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyclass'):
            context['self'].bodyclass(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'middleclass'):
            context['self'].middleclass(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('&mdash; Portal')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if user.groups.filter(name='Prescribers').exists():
            __M_writer('<p class = "doctitle">Prescriber Portal</p>\r\n')
        else:
            if user.groups.filter(name='HealthOfficials').exists():
                __M_writer('    <p class = "offtitle">Health Official Portal</p>\r\n')
            else:
                if user.groups.filter(name='HHS').exists():
                    __M_writer('        <p class = "hhstitle">Data Clerk Portal</p>\r\n')
                else:
                    __M_writer('        <p class = "portaltitle">Portal</p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodyclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodyclass():
            return render_bodyclass(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if user.groups.filter(name='Prescribers').exists():
            __M_writer('<body class="docbod">\r\n')
        else:
            if user.groups.filter(name='HHS').exists():
                __M_writer('        <body class="hhsbod">\r\n')
            else:
                if user.groups.filter(name='HealthOfficials').exists() or user.groups.filter(name='Officials').exists:
                    __M_writer('        <body class="offbod">\r\n')
                else:
                    __M_writer('        <body class="site_middle">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_middleclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def middleclass():
            return render_middleclass(context)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if user.groups.filter(name='Prescribers').exists():
            __M_writer('<div class="doccontent">\r\n')
        else:
            if user.groups.filter(name='HealthOfficials').exists():
                __M_writer('    <div class="offcontent">\r\n')
            else:
                if user.groups.filter(name='HHS').exists():
                    __M_writer('        <div class="hhscontent">\r\n')
                else:
                    __M_writer('        <div class="site_middle">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/intexsite/portal/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "49": 1, "50": 2, "55": 5, "60": 23, "65": 39, "70": 43, "75": 59, "80": 62, "86": 5, "92": 5, "98": 8, "105": 8, "106": 10, "107": 11, "108": 12, "109": 13, "110": 14, "111": 15, "112": 16, "113": 17, "114": 18, "115": 19, "121": 25, "128": 25, "129": 26, "130": 27, "131": 28, "132": 29, "133": 30, "134": 31, "135": 32, "136": 33, "137": 34, "138": 35, "144": 42, "150": 42, "156": 45, "163": 45, "164": 46, "165": 47, "166": 48, "167": 49, "168": 50, "169": 51, "170": 52, "171": 53, "172": 54, "173": 55, "179": 61, "185": 61, "191": 185}}
__M_END_METADATA
"""
