# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554856051.05276
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/portal/templates/search.html'
_template_uri = 'search.html'
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
        def left_content():
            return render_left_content(context._locals(__M_locals))
        msg = context.get('msg', UNDEFINED)
        form = context.get('form', UNDEFINED)
        form2 = context.get('form2', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n')
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
        __M_writer('&mdash; Search')
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
        msg = context.get('msg', UNDEFINED)
        form = context.get('form', UNDEFINED)
        form2 = context.get('form2', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def site_content():
            return render_site_content(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.has_perm('account.search') or request.user.has_perm('account.safesearch'):
            __M_writer('   <div class="content">\r\n      <p class="portaltitle">Search</p>\r\n      <p class="message">')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(msg))
            __M_writer('</p>\r\n      <form action="" method="post">\r\n            <table >\r\n               <tr>\r\n                  <td style="width:2%"></td>\r\n                  <td style="width:50%" >\r\n                     <table class="formlabel">\r\n                           ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form ))
            __M_writer('\r\n                     </table>\r\n                  </td>\r\n                  <td style="border-left-color:grey;border-left-style:solid;border-width:1px; width: 10px"></td>\r\n                  <td style="width:5%"></td>\r\n                  <td style="width:50%">\r\n                     <table class="formlabel"style="vertical-align:top; margin-bottom:165px;">\r\n                         ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(form2))
            __M_writer('\r\n                     </table>\r\n                  </td>\r\n                  <td style="width:3px"></td>\r\n               </tr>\r\n            \r\n            </table>\r\n            <hr>\r\n            \r\n            <p style="margin-left:45%; margin-top:15px;"><input type="submit" class="btn mybtn" value="Search"/></p>\r\n          </form>\r\n   </div>\r\n')
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
{"filename": "C:/Users/Isaac/intexsite/portal/templates/search.html", "uri": "search.html", "source_encoding": "utf-8", "line_map": {"29": 0, "47": 1, "52": 3, "57": 6, "62": 39, "72": 3, "78": 3, "84": 4, "90": 4, "96": 8, "107": 8, "108": 9, "109": 10, "110": 12, "111": 12, "112": 19, "113": 19, "114": 26, "115": 26, "121": 41, "127": 41, "133": 127}}
__M_END_METADATA
"""
