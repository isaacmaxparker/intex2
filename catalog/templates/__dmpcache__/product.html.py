# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1553111405.2969582
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
        message = context.get('message', UNDEFINED)
        quant = context.get('quant', UNDEFINED)
        self = context.get('self', UNDEFINED)
        price = context.get('price', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        name = context.get('name', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        desc = context.get('desc', UNDEFINED)
        imageurls = context.get('imageurls', UNDEFINED)
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
        message = context.get('message', UNDEFINED)
        quant = context.get('quant', UNDEFINED)
        self = context.get('self', UNDEFINED)
        price = context.get('price', UNDEFINED)
        def site_content():
            return render_site_content(context)
        name = context.get('name', UNDEFINED)
        desc = context.get('desc', UNDEFINED)
        imageurls = context.get('imageurls', UNDEFINED)
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
        __M_writer(' left!\r\n                   </p>\r\n\r\n                   <form style="vertical-align:middle;" method="POST" id="productform">\r\n\r\n                   \r\n                    <label class="formlabel" style="font-size:18px;">Quantity:</label>\r\n                    <input type="number" value="0" class="forminput col-sm-2" step="1" style="margin:10px;" name="QuantOrd">\r\n                    \r\n                    <input type="submit" class="btn btn-lg buybtn" value="Buy Now">\r\n\r\n                   </form>\r\n')
        if message != '':
            __M_writer('                    <div id="maintenence" class = "alert alert-danger" style="">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(message))
            __M_writer('</div>\r\n')
        __M_writer('                   <div style="padding-top:20px;">\r\n                   <a class="btn mybtn btn-sm" href="/catalog/index/-/1">Back to products</a>\r\n                </div>\r\n               </div>\r\n            </td>\r\n        </tr>\r\n    </table>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/catalog/templates/product.html", "uri": "product.html", "source_encoding": "utf-8", "line_map": {"29": 0, "45": 1, "50": 6, "55": 61, "61": 4, "67": 4, "73": 8, "86": 8, "87": 14, "88": 15, "89": 15, "90": 15, "91": 17, "92": 22, "93": 22, "94": 27, "95": 27, "96": 30, "97": 30, "98": 33, "99": 33, "100": 36, "101": 36, "102": 48, "103": 49, "104": 49, "105": 49, "106": 51, "112": 106}}
__M_END_METADATA
"""
