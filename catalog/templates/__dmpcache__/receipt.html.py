# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553884993.1963887
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/catalog/templates/receipt.html'
_template_uri = 'receipt.html'
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
        round = context.get('round', UNDEFINED)
        total = context.get('total', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        subtotal = context.get('subtotal', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        tax = context.get('tax', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        saleItems = context.get('saleItems', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        __M_writer('\r\nReciept\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        round = context.get('round', UNDEFINED)
        total = context.get('total', UNDEFINED)
        self = context.get('self', UNDEFINED)
        subtotal = context.get('subtotal', UNDEFINED)
        def site_content():
            return render_site_content(context)
        saleItems = context.get('saleItems', UNDEFINED)
        tax = context.get('tax', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div id="content">\r\n    <p class="paragraph">\r\n        Thank you for shopping with FOMO! \r\n        <a href="/homepage/contact/" class="link">Let us know how we did!</a>\r\n        <hr>\r\n    </p>\r\n    <table class="carttab" width=100%; style="text-align:center;">\r\n        <tr>\r\n            <th>\r\n                &nbsp;\r\n            </th>\r\n            <th>\r\n                Product Name\r\n            </th>\r\n            <th>\r\n                Quantity\r\n            </th>\r\n            <th>\r\n                Price\r\n            </th>\r\n            <th>\r\n                Extended\r\n            </th>\r\n        </tr>\r\n')
        for item in saleItems :
            __M_writer('        <tr>\r\n            <td>\r\n                <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.image_url()))
            __M_writer('" class="cartimg">\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.product.name))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(item.quantity))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                    $')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(round(item.price,2)))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                    $')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(round(item.price * item.quantity,2)))
            __M_writer('\r\n            </td>\r\n        </tr>\r\n')
        __M_writer('        \r\n        <tr>\r\n                <td>\r\n                    &nbsp;\r\n                </td>\r\n                <td>\r\n                        &nbsp;\r\n                </td>\r\n                <td>\r\n                    &nbsp;\r\n                </td>\r\n                <td>\r\n                    <b>Subtotal</b>\r\n                </td>\r\n                <td>\r\n                    $')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(subtotal))
        __M_writer('\r\n                </td>\r\n                <td>\r\n                     &nbsp;\r\n                </td>\r\n    \r\n            </tr>\r\n        \r\n        <tr>\r\n            <td>\r\n                &nbsp;\r\n            </td>\r\n            <td>\r\n                    &nbsp;\r\n            </td>\r\n            <td>\r\n                &nbsp;\r\n            </td>\r\n            <td>\r\n                <b>Tax</b>\r\n            </td>\r\n            <td>\r\n                $')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(tax))
        __M_writer('\r\n            </td>\r\n            <td>\r\n                 &nbsp;\r\n            </td>\r\n\r\n        </tr>\r\n        <tr>\r\n                <td>&nbsp;</td>\r\n                <td>&nbsp;</td>\r\n                <td>&nbsp;</td>\r\n                <td><hr></td>\r\n                <td><hr></td>\r\n \r\n\r\n        </tr>\r\n        <tr style="font-size:24px;">\r\n            \r\n                <td>\r\n                    &nbsp;\r\n                </td>\r\n                <td>\r\n                    \r\n                </td>\r\n                <td>\r\n                    &nbsp;\r\n                </td>\r\n                <td>\r\n                        <b><em>Total</em></b>\r\n                </td>\r\n                <td>\r\n                   $')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(total))
        __M_writer('\r\n                </td>\r\n                <td>\r\n                     &nbsp;\r\n                </td>\r\n    \r\n            </tr>\r\n    </table>\r\n</div>\r\n')
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
{"filename": "C:/Users/Isaac/mysite/catalog/templates/receipt.html", "uri": "receipt.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "48": 1, "49": 2, "54": 6, "59": 129, "69": 4, "75": 4, "81": 8, "93": 8, "94": 33, "95": 34, "96": 36, "97": 36, "98": 39, "99": 39, "100": 42, "101": 42, "102": 45, "103": 45, "104": 48, "105": 48, "106": 52, "107": 67, "108": 67, "109": 89, "110": 89, "111": 120, "112": 120, "118": 131, "124": 131, "130": 124}}
__M_END_METADATA
"""
