# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1551903920.3814645
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/catalog/templates/product.html'
_template_uri = 'product.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_header_title', 'site_content']


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
        name = context.get('name', UNDEFINED)
        desc = context.get('desc', UNDEFINED)
        price = context.get('price', UNDEFINED)
        imageurls = context.get('imageurls', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        quant = context.get('quant', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\nProduct Details\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        name = context.get('name', UNDEFINED)
        def site_content():
            return render_site_content(context)
        desc = context.get('desc', UNDEFINED)
        self = context.get('self', UNDEFINED)
        price = context.get('price', UNDEFINED)
        quant = context.get('quant', UNDEFINED)
        imageurls = context.get('imageurls', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="content">\r\n    <table>\r\n        <tr>\r\n            <td width="33%">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(imageurls[0]))
        __M_writer('" class="prodimg">\r\n            </td>\r\n            <td width="10px">\r\n                &nbsp;\r\n            </td>\r\n            <td width="33%">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(imageurls[1]))
        __M_writer('" class="prodimg">\r\n            </td>\r\n            <td width="34%">\r\n               <div class="prodinfo">\r\n                   <p class="prodtitle">\r\n                        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(name))
        __M_writer('\r\n                   </p>\r\n                   <p class="proddesc">\r\n                        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(desc))
        __M_writer('\r\n                   </p>\r\n                   <p class="prodprice">\r\n                        $')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(price))
        __M_writer('\r\n                   </p>\r\n                   <p class="prodquant">\r\n                       Only ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(quant))
        __M_writer(' left!\r\n                   </p>\r\n               </div>\r\n            </td>\r\n        </tr>\r\n    </table>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/catalog/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 6, "54": 43, "60": 4, "66": 4, "72": 8, "84": 8, "85": 14, "86": 14, "87": 20, "88": 20, "89": 25, "90": 25, "91": 28, "92": 28, "93": 31, "94": 31, "95": 34, "96": 34, "102": 96}}
__M_END_METADATA
"""
