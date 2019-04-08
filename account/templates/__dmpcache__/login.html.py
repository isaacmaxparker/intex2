# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554763930.6327603
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/account/templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_header_title', 'logo', 'page_title', 'left_content', 'site_content', 'right_content']


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
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        type = context.get('type', UNDEFINED)
        def logo():
            return render_logo(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'logo'):
            context['self'].logo(**pageargs)
        

        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        type = context.get('type', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if type == '1':
            __M_writer('        <p>Prescriber Login</p>\r\n')
        if type == '2':
            __M_writer('        <p>Health Official Login</p>\r\n')
        if type == '3':
            __M_writer('        <p>HHA Clerk Login</p>\r\n')
        if type == '4':
            __M_writer('        <p>Login</p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_logo(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def logo():
            return render_logo(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/logo.png" alt="python" />\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('&mdash; Login')
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
        form = context.get('form', UNDEFINED)
        def site_content():
            return render_site_content(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content" style="margin-left:25%; padding-right:25%; width: 50%">\r\n        \r\n        <form action="" method="post">\r\n            <table class="formlabel">\r\n            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form ))
        __M_writer('\r\n            </table>\r\n            <p style="margin-left:80%; margin-top:15px;"><input type="submit" class="btn mybtn" value="Login"/></p>\r\n          </form>\r\n\r\n      </div>\r\n')
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
{"filename": "C:/Users/Isaac/intexsite/account/templates/login.html", "uri": "login.html", "source_encoding": "utf-8", "line_map": {"29": 0, "50": 1, "55": 16, "60": 19, "65": 20, "70": 24, "75": 38, "85": 3, "92": 3, "93": 4, "94": 5, "95": 7, "96": 8, "97": 10, "98": 11, "99": 13, "100": 14, "106": 17, "114": 17, "115": 18, "116": 18, "122": 20, "128": 20, "134": 22, "140": 22, "146": 27, "154": 27, "155": 32, "156": 32, "162": 40, "168": 40, "174": 168}}
__M_END_METADATA
"""
