# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1551896641.4403906
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/account/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_header_title', 'page_title', 'left_content', 'site_content', 'right_content']


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
        def right_content():
            return render_right_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
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
        __M_writer('\r\nMy Account\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('&mdash; Account')
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
        request = context.get('request', UNDEFINED)
        def site_content():
            return render_site_content(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="content">\r\n        <div></div>\r\n<table width="50%" style="text-align:left;">\r\n        <tr><td><img src="/static/homepage/media/UserImages/')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
        __M_writer('.jpg" class="userimage"></td>\r\n                <th style="text-align:right; padding-right: 10px;" class="formlabel">\r\n                        Name:\r\n                    </th>\r\n            <td class="forminput" style="border-style:none">\r\n                    ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.first_name))
        __M_writer(' ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.last_name))
        __M_writer(' \r\n            </td>\r\n        </tr>\r\n       <tr><td><hr></td><td><hr></td></tr>\r\n<tr>\r\n        <td></td>\r\n        <th style="text-align:right; padding-right: 10px;", class="formlabel">\r\n                Username:\r\n            </th>\r\n    <td class="forminput" style="border-style:none">\r\n        \r\n            ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
        __M_writer(' \r\n        \r\n    </td>\r\n</tr>\r\n<tr>\r\n        <td></td>\r\n        <th style="text-align:right; padding-right: 10px;" class="formlabel">\r\n                Email:\r\n            </th>\r\n    <td class="forminput" style="border-style:none">')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.email))
        __M_writer(' \r\n    </td>\r\n</tr>\r\n      \r\n<tr>\r\n        <td></td>\r\n                <th style="text-align:right; padding-right: 10px;" class="formlabel">\r\n                        \r\n                    </th>\r\n            <td class="forminput" style="border-style:none"><a href="/account/index/">Change Password</a>\r\n            </td>\r\n        </tr>\r\n</table>\r\n</div>\r\n<br><br>\r\n')
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
{"filename": "C:/Users/Isaac/mysite/account/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "46": 1, "51": 5, "56": 7, "61": 11, "66": 58, "76": 3, "82": 3, "88": 7, "94": 7, "100": 9, "106": 9, "112": 14, "120": 14, "121": 18, "122": 18, "123": 23, "124": 23, "125": 23, "126": 23, "127": 34, "128": 34, "129": 43, "130": 43, "136": 60, "142": 60, "148": 142}}
__M_END_METADATA
"""
