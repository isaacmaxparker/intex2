# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1551896756.845706
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/homepage/templates/contact.html'
_template_uri = 'contact.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'left_content', 'page_header_title', 'site_content', 'bodclass']


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
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        def bodclass():
            return render_bodclass(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        msg = context.get('msg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('&mdash; Contact')
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


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\nContact Isaac\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        msg = context.get('msg', UNDEFINED)
        def site_content():
            return render_site_content(context)
        def bodclass():
            return render_bodclass(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodclass'):
            context['self'].bodclass(**pageargs)
        

        __M_writer('\r\n\r\n<div class="content">\r\n<p class="alert">\r\n    ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(msg))
        __M_writer('\r\n</p>\r\n\r\n\r\n<form method="POST" id="contactform">\r\n    <table class="content" style="margin-left:25%; padding-right:25%; width: 50%">\r\n        <tr>\r\n            <td>\r\n                    <p class="formlabel"> Name: </p> \r\n            </td>\r\n            <td>\r\n                    <input type="text" name="yourname" class="forminput"/> \r\n                </td>\r\n        </tr>\r\n        <tr>\r\n                <td>\r\n                        <p class="formlabel"> Email:  </p>\r\n                </td>\r\n                <td>\r\n                        <input type = "email" name="youremail" class="forminput" />\r\n                    </td>\r\n            </tr>\r\n            <tr>\r\n                    <td>\r\n                            <p class="formlabel"> Message:  </p>\r\n                    </td>\r\n                    <td>\r\n                            <input type="text"  name="yourmessage" class="forminput" />\r\n                        </td>\r\n                </tr>\r\n                \r\n                \r\n    </table>\r\n  \r\n    <p style="margin-left:40%; margin-top:15px;"><input type="submit" class="btn btn-outline-secondary mybtn"/></p>\r\n    \r\n  \r\n</form>\r\n<br><br>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodclass():
            return render_bodclass(context)
        __M_writer = context.writer()
        __M_writer('\r\nclass="backtimef"\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/homepage/templates/contact.html", "uri": "contact.html", "source_encoding": "utf-8", "line_map": {"29": 0, "46": 1, "51": 3, "56": 7, "61": 11, "66": 63, "72": 3, "78": 3, "84": 5, "90": 5, "96": 9, "102": 9, "108": 13, "118": 13, "123": 17, "124": 21, "125": 21, "131": 15, "137": 15, "143": 137}}
__M_END_METADATA
"""
