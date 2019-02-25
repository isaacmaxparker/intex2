# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550692249.8658702
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/account/templates/app_base.htm'
_template_uri = '/account/templates/app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['navbar_items', 'left_content']


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
    return runtime._inherit_from(context, '../../homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def navbar_items():
            return render_navbar_items(context)
        __M_writer = context.writer()
        __M_writer('\r\n                <li class="mynav-item">\r\n                      <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='index' else ' '))
        __M_writer('"  href="/">Home</a>\r\n                    </li>\r\n                    <li class="mynav-item">\r\n                        <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='contact' else ' '))
        __M_writer('" href="/contact/">Contact</a>\r\n                      </li>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<ul>\r\n    <li class="mynav-item">\r\n        <a class="nav-link " data-toggle="tab" href="/">Home</a>\r\n      </li>\r\n      <li class="mynav-item">\r\n          <a class="nav-link " data-toggle="tab" href="/contact/">Contact</a>\r\n        </li>\r\n</ul>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/account/templates/app_base.htm", "uri": "/account/templates/app_base.htm", "source_encoding": "utf-8", "line_map": {"29": 0, "40": 1, "45": 12, "50": 25, "56": 5, "64": 5, "65": 7, "66": 7, "67": 10, "68": 10, "74": 14, "80": 14, "86": 80}}
__M_END_METADATA
"""
