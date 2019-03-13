# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552438486.1379445
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_header_title', 'site_content', 'right_content']


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
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        category = context.get('category', UNDEFINED)
        products = context.get('products', UNDEFINED)
        page = context.get('page', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        numpages = context.get('numpages', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n\r\n')
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
        category = context.get('category', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'Catalog' if category is None else category.name))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        category = context.get('category', UNDEFINED)
        products = context.get('products', UNDEFINED)
        page = context.get('page', UNDEFINED)
        numpages = context.get('numpages', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_content():
            return render_site_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div id="content" style="margin:0 0px;">\r\n')
        for product in products:
            __M_writer('        <span class="product_container" data-product-id="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.id))
            __M_writer('"></span>\r\n')
        __M_writer('\r\n    <table class="nextprev" width=100%>\r\n        <tr>\r\n            <td style="float:right; margin-right: 0;">\r\n')
        if page-1 != 0:
            __M_writer('                    <a class="btn btn-lg mybtn" href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(category if category is not None else '-'))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page-1))
            __M_writer('">Previous</a>\r\n')
        __M_writer('            </td>\r\n        \r\n            <td width=50%>       \r\n')
        if page != numpages:
            __M_writer('                <a class="btn mybtn btn-lg" href="/catalog/index/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(category if category is not None else '-'))
            __M_writer('/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(page+1))
            __M_writer('">Next</a>\r\n')
        __M_writer('            </td>\r\n        </tr>\r\n    </table>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<p class="quote">\r\n    "On Wednesdays we wear pink"<br>\r\n    - Karen Smith\r\n\r\n    \r\n</p>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "47": 1, "48": 2, "53": 6, "58": 30, "68": 4, "76": 4, "77": 5, "78": 5, "84": 8, "95": 8, "96": 10, "97": 11, "98": 11, "99": 11, "100": 13, "101": 17, "102": 18, "103": 18, "104": 18, "105": 18, "106": 18, "107": 20, "108": 23, "109": 24, "110": 24, "111": 24, "112": 24, "113": 24, "114": 26, "120": 32, "126": 32, "132": 126}}
__M_END_METADATA
"""
