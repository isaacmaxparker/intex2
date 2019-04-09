# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554828175.7591279
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/homepage/templates/contact.html'
_template_uri = 'contact.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'left_content', 'page_header_title', 'site_content']


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
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        msg = context.get('msg', UNDEFINED)
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
        __M_writer('\r\nContact STOP.GOV\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_content():
            return render_site_content(context)
        msg = context.get('msg', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="content">\r\n<p class="alert">\r\n    ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(msg))
        __M_writer('\r\n</p>\r\n\r\n\r\n<form method="POST" id="contactform">\r\n    <table class="content formlabel" style="margin-left:15%; padding-right:25%; width: 50%">\r\n        <tr>\r\n            <td>\r\n                    <p class="formlabel"> Name: </p> \r\n            </td>\r\n            <td>\r\n                    <input type="text" name="yourname" value="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.first_name + ' ' + request.user.last_name if request.user.is_authenticated else ''))
        __M_writer('"/> \r\n                </td>\r\n        </tr>\r\n        <tr>\r\n                <td>\r\n                        <p class="formlabel"> Email:  </p>\r\n                </td>\r\n                <td>\r\n                        <input type = "email" name="youremail" value="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.email if request.user.is_authenticated else ''))
        __M_writer('" />\r\n                    </td>\r\n            </tr>\r\n            <tr>\r\n                    <td>\r\n                            <p class="formlabel"> Message:  </p>\r\n                    </td>\r\n                    <td><textarea name="yourmessage" class="forminput"></textarea>\r\n                            \r\n                        </td>\r\n                </tr>     \r\n    </table>\r\n    <p style="margin-left:40%; margin-top:15px;"><input type="submit" class="btn btn-outline-secondary mybtn"/></p>\r\n</form>\r\n<br><br>\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/intexsite/homepage/templates/contact.html", "uri": "contact.html", "source_encoding": "utf-8", "line_map": {"29": 0, "45": 1, "50": 3, "55": 7, "60": 11, "65": 54, "71": 3, "77": 3, "83": 5, "89": 5, "95": 9, "101": 9, "107": 13, "116": 13, "117": 17, "118": 17, "119": 28, "120": 28, "121": 36, "122": 36, "128": 122}}
__M_END_METADATA
"""
