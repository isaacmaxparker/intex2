# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555028390.4660912
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/portal/templates/remove.html'
_template_uri = 'remove.html'
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
        exists = context.get('exists', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        name = context.get('name', UNDEFINED)
        msg = context.get('msg', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        gender = context.get('gender', UNDEFINED)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        exists = context.get('exists', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        name = context.get('name', UNDEFINED)
        msg = context.get('msg', UNDEFINED)
        def site_content():
            return render_site_content(context)
        form = context.get('form', UNDEFINED)
        gender = context.get('gender', UNDEFINED)
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.is_authenticated:
            __M_writer('<div class="content">\r\n      <div style="width:100%;margin-left:23%">\r\n       <form action="" method="POST">\r\n        <p class="homeparg">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(msg))
            __M_writer('</p>\r\n')
            if exists:
                __M_writer('        <p class="link2" style="margin-left:13%;font-style:italic">Type "Delete" below to confirm</p>\r\n        <div class="linkbox hha" style="margin-left:-150px;width:auto;max-width: 800px">\r\n                <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/UserImages/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(gender))
                __M_writer('.png">\r\n                <p class="hha">')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(name))
                __M_writer('</p> \r\n        </div>\r\n         <table class="formlabel" style="width:100%;margin-left:10%">\r\n             ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form))
                __M_writer('\r\n         </table>\r\n         <p style="margin-left:20%; margin-top:15px;"><input type="submit" class="btn mybtn" value="Update"/></p>\r\n')
            __M_writer('       </form>\r\n     </div>\r\n </div>\r\n')
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
{"filename": "C:/Users/Isaac/intexsite/portal/templates/remove.html", "uri": "remove.html", "source_encoding": "utf-8", "line_map": {"29": 0, "50": 1, "55": 3, "60": 7, "65": 30, "75": 3, "81": 3, "87": 5, "93": 5, "99": 9, "113": 9, "114": 10, "115": 11, "116": 14, "117": 14, "118": 15, "119": 16, "120": 18, "121": 18, "122": 18, "123": 18, "124": 19, "125": 19, "126": 22, "127": 22, "128": 26, "134": 32, "140": 32, "146": 140}}
__M_END_METADATA
"""
