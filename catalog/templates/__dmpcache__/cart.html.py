# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553719750.531263
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/catalog/templates/cart.html'
_template_uri = 'cart.html'
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
        def site_content():
            return render_site_content(context._locals(__M_locals))
        tax = context.get('tax', UNDEFINED)
        total = context.get('total', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        saleItems = context.get('saleItems', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
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
        __M_writer = context.writer()
        __M_writer('\r\nCart\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_content():
            return render_site_content(context)
        tax = context.get('tax', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        total = context.get('total', UNDEFINED)
        saleItems = context.get('saleItems', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div id="content">\r\n    <table class="carttab" width=100%; style="text-align:center;">\r\n        <tr>\r\n            <th>\r\n                &nbsp;\r\n            </th>\r\n            <th>\r\n                Product Name\r\n            </th>\r\n            <th>\r\n                Quantity\r\n            </th>\r\n            <th>\r\n                Price\r\n            </th>\r\n            <th>\r\n                Extended\r\n            </th>\r\n            <th>Actions</th>\r\n        </tr>\r\n')
        for item in saleItems :
            __M_writer('        <tr>\r\n            <td>\r\n                <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.image_url()))
            __M_writer('" class="cartimg">\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.name))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.quantity))
            __M_writer('\r\n            </td>\r\n            <td>\r\n               $')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.price / item.quantity))
            __M_writer('\r\n            </td>\r\n            <td>\r\n               $')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.price))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                <a class="rmv" href="/catalog/cart.remove/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.id))
            __M_writer('/">Remove</a>\r\n            </td>\r\n        </tr>\r\n')
        __M_writer('        <tr >\r\n            <td>\r\n                &nbsp;\r\n            </td>\r\n            <td>\r\n                Tax\r\n            </td>\r\n            <td>\r\n                &nbsp;\r\n            </td>\r\n            <td>\r\n                &nbsp;\r\n            </td>\r\n            <td>\r\n                $')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(tax))
        __M_writer('\r\n            </td>\r\n            <td>\r\n                 &nbsp;\r\n            </td>\r\n\r\n        </tr>\r\n        <tr>\r\n                <td>\r\n                    &nbsp;\r\n                </td>\r\n                <td>\r\n                    Total\r\n                </td>\r\n                <td>\r\n                    &nbsp;\r\n                </td>\r\n                <td>\r\n                    &nbsp;\r\n                </td>\r\n                <td>\r\n                   $')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(total))
        __M_writer('\r\n                </td>\r\n                <td>\r\n                     &nbsp;\r\n                </td>\r\n    \r\n            </tr>\r\n    </table>\r\n<div style="align-content:center;"></div>\r\n<a class="btn btn-lg buybtn" style="margin-left:42%;" href="/catalog/checkout/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(cart.id))
        __M_writer('">Checkout Now</a>\r\n</div>\r\n</div>\r\n')
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
{"filename": "C:/Users/Isaac/mysite/catalog/templates/cart.html", "uri": "cart.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "47": 1, "48": 2, "53": 6, "58": 98, "68": 4, "74": 4, "80": 8, "91": 8, "92": 29, "93": 30, "94": 32, "95": 32, "96": 35, "97": 35, "98": 38, "99": 38, "100": 41, "101": 41, "102": 44, "103": 44, "104": 47, "105": 47, "106": 51, "107": 65, "108": 65, "109": 86, "110": 86, "111": 95, "112": 95, "118": 100, "124": 100, "130": 124}}
__M_END_METADATA
"""