# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555045661.358058
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/account/templates/changepass.html'
_template_uri = 'changepass.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'left_content', 'site_content', 'right_content']


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
        self = context.get('self', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        msg = context.get('msg', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

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
        form = context.get('form', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_content():
            return render_site_content(context)
        msg = context.get('msg', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.is_authenticated:
            __M_writer('   <div class="content">\r\n     <div style="width:100%;margin-left:18%">\r\n      <form action="" method="POST">\r\n        <p style="padding-top:10px;font-weight: bold;font-size: 56px;color:grey;line-height: 40px;">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
            __M_writer('</p>\r\n        <br>\r\n        ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(msg))
            __M_writer('\r\n        <table class="formlabel">\r\n            ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form))
            __M_writer('\r\n        </table>\r\n        <p style="margin-left:20%; margin-top:15px;"><input type="submit" class="btn mybtn" value="Change Password"/></p>\r\n      </form>\r\n    </div>\r\n</div>\r\n')
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
{"filename": "C:/Users/Isaac/intexsite/account/templates/changepass.html", "uri": "changepass.html", "source_encoding": "utf-8", "line_map": {"29": 0, "46": 1, "51": 3, "56": 7, "61": 25, "71": 3, "77": 3, "83": 5, "89": 5, "95": 9, "105": 9, "106": 10, "107": 11, "108": 14, "109": 14, "110": 16, "111": 16, "112": 18, "113": 18, "119": 27, "125": 27, "131": 125}}
__M_END_METADATA
"""
