# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555028497.9312081
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/portal/templates/listings.html'
_template_uri = 'listings.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'site_content']


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
        request = context.get('request', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

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
        __M_writer('&mdash; Home')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def site_content():
            return render_site_content(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n   <div class="content">\r\n    <div class="homeparg" style="width:50%;margin-left:25%">\r\n        <span style="font-size:40px; font-weight: bold;">Hello ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.first_name))
        __M_writer('! </span>\r\n         <br>What are you trying to do? <br>\r\n         <br>\r\n         <p><a class="link2" href="/portal/create/">Create a new prescriber</a></p>\r\n             <p>Edit an existing prescriber</p>\r\n             <p style="font-size:18px; padding-left:10%">Search for an existing prescriber <a href="/portal/search/" class="link2">here</a> first</p>\r\n             <p>Delete an existing prescriber</p>\r\n             <p style="font-size:18px; padding-left:10%">Search for an existing prescriber <a href="/portal/search/" class="link2">here</a> first</p>\r\n        <p><a class="link2" href="/portal/create/">Create a new Prescription</a></p>\r\n             <p>Edit an existing prescriber</p>\r\n             <p style="font-size:18px; padding-left:10%">Search for an existing prescriber <a href="/portal/search/" class="link2">here</a> first</p>\r\n             <p>Delete an existing prescriber</p>\r\n             <p style="font-size:18px; padding-left:10%">Search for an existing prescriber <a href="/portal/search/" class="link2">here</a> first</p>\r\n         \r\n</div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/intexsite/portal/templates/listings.html", "uri": "listings.html", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 3, "50": 24, "56": 3, "62": 3, "68": 5, "76": 5, "77": 8, "78": 8, "84": 78}}
__M_END_METADATA
"""
