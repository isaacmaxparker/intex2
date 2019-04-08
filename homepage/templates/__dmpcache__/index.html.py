# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554763918.6981897
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'bodclass', 'left_content', 'site_content', 'right_content']


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
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def bodclass():
            return render_bodclass(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodclass'):
            context['self'].bodclass(**pageargs)
        

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


def render_bodclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodclass():
            return render_bodclass(context)
        __M_writer = context.writer()
        __M_writer('\r\nclass="back2"\r\n')
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
        def site_content():
            return render_site_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n     <p class="homeparg"><span style="font-size:40px; font-weight: bold;">Welcome to STOP.gov! </span>This online portal will help government agencies and providers work together to decrease America\'s opiod epidemic. Login to start today!</p>\r\n     <br><hr><br>\r\n     <p style="text-align:center;font-family:century gothic; font-size:36px;">I am a:</p>\r\n     <a href="$/account/login/1/" class="alinkbox">\r\n     <div class="linkbox prov">\r\n        <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/avatar.png">\r\n        <p class="prov">Prescriber</p>\r\n     </div>\r\n    </a>\r\n    <a href="/account/login/2/" class="alinkbox">\r\n     <div class="linkbox gov">\r\n        <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/heart.png">\r\n        <p class="gov">Health Official</p>\r\n     </div>\r\n    </a>\r\n     <a href="/account/login/3/" class="alinkbox">\r\n     <div class="linkbox hha">\r\n        <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/HHA.png">\r\n        <p class="hha">HHA Clerk</p>\r\n     </div>\r\n    </a>\r\n   \r\n<br>\r\n<hr>\r\n\r\n    </div>\r\n')
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
{"filename": "C:/Users/Isaac/intexsite/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "46": 1, "51": 3, "56": 7, "61": 11, "66": 41, "76": 3, "82": 3, "88": 5, "94": 5, "100": 9, "106": 9, "112": 13, "120": 13, "121": 20, "122": 20, "123": 26, "124": 26, "125": 32, "126": 32, "132": 43, "138": 43, "144": 138}}
__M_END_METADATA
"""
