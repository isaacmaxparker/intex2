# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1552437066.5734427
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/catalog/templates/product.tile.html'
_template_uri = 'product.tile.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['content']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        product = context.get('product', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        product = context.get('product', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<a href="/catalog/product/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.id))
        __M_writer('">\r\n    <div class="product-tile">\r\n        <div ><img class="product-image" src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.image_url()))
        __M_writer('"></div>\r\n        <div class="product-name">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.name))
        __M_writer('</div>\r\n        <div class="product-price">$')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(product.price))
        __M_writer('</div>   \r\n    </div>\r\n</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/catalog/templates/product.tile.html", "uri": "product.tile.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "48": 2, "56": 2, "57": 3, "58": 3, "59": 5, "60": 5, "61": 6, "62": 6, "63": 7, "64": 7, "70": 64}}
__M_END_METADATA
"""
