# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552447765.745767
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
        imageurls = context.get('imageurls', UNDEFINED)
        price = context.get('price', UNDEFINED)
        name = context.get('name', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        desc = context.get('desc', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        quant = context.get('quant', UNDEFINED)
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
        imageurls = context.get('imageurls', UNDEFINED)
        price = context.get('price', UNDEFINED)
        desc = context.get('desc', UNDEFINED)
        name = context.get('name', UNDEFINED)
        def site_content():
            return render_site_content(context)
        self = context.get('self', UNDEFINED)
        quant = context.get('quant', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="content">\r\n    <table>\r\n        <tr>\r\n            <td width="8%" height="auto" class="parent">\r\n')
        for img in imageurls:
            __M_writer('                <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(img))
            __M_writer('" class="prodimg">\r\n')
        __M_writer('            </td>\r\n            <td width="10px">\r\n                &nbsp;\r\n            </td>\r\n            <td width="38%">\r\n                <img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(imageurls[0]))
        __M_writer('" class="prodimgmain">\r\n            </td>\r\n            <td width="55%">\r\n               <div class="prodinfo">\r\n                   <p class="prodtitle">\r\n                        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(name))
        __M_writer('\r\n                   </p>\r\n                   <p class="proddesc">\r\n                        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(desc))
        __M_writer('\r\n                   </p>\r\n                   <p class="prodprice">\r\n                        $')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(price))
        __M_writer('\r\n                   </p>\r\n                   <p class="prodquant">\r\n                       Only ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(quant))
        __M_writer(' left!\r\n                   </p>\r\n                   <a class="btn mybtn btn-lg" href="/catalog/index/-/1">Back to products</a>\r\n               </div>\r\n            </td>\r\n        </tr>\r\n    </table>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/catalog/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"29": 0, "44": 1, "49": 6, "54": 46, "60": 4, "66": 4, "72": 8, "84": 8, "85": 14, "86": 15, "87": 15, "88": 15, "89": 17, "90": 22, "91": 22, "92": 27, "93": 27, "94": 30, "95": 30, "96": 33, "97": 33, "98": 36, "99": 36, "105": 99}}
__M_END_METADATA
"""
