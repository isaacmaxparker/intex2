# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554771485.6903293
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'bodclass', 'left_content', 'site_content', 'right_content']


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
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def bodclass():
            return render_bodclass(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodclass'):
            context['self'].bodclass(**pageargs)
        

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


def render_bodclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodclass():
            return render_bodclass(context)
        __M_writer = context.writer()
        __M_writer('\r\nclass="back2"\r\n')
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.is_authenticated:
            __M_writer('   <div class="content">\r\n         <p class="homeparg"><span style="font-size:40px; font-weight: bold;">Welcome to STOP.gov! </span>This online portal will help government agencies and providers work together to decrease America\'s opiod epidemic. Let\'s start fixing today!</p>  \r\n')
            if request.user.has_perm('account.search'):
                __M_writer('         <a href="/account/login/3/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/pill3.png">\r\n               <p class="hha">Search Drugs</p>\r\n            </div>\r\n           </a>\r\n           <a href="/account/login/3/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/people.png">\r\n               <p style="color:#33BDA6">Search Providers</p>\r\n            </div>\r\n           </a>\r\n')
            if request.user.has_perm('account.safesearch'):
                __M_writer('         <a href="/account/login/3/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/pill3.png">\r\n               <p class="hha">Search Drugs</p>\r\n            </div>\r\n           </a>\r\n         <a href="/account/login/3/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/HHA.png">\r\n               <p class="hha" style="color:#33BDA6">Search Providers</p>\r\n            </div>\r\n           </a>\r\n')
            if request.user.has_perm('account.analytics'):
                __M_writer('         <a href="/account/login/3/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/HHA.png">\r\n               <p class="hha">View Analytics</p>\r\n            </div>\r\n           </a>\r\n')
            if request.user.has_perm('account.CRUD'):
                __M_writer('         <a href="/account/login/3/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/HHA.png">\r\n               <p class="hha">Edit Listings</p>\r\n            </div>\r\n           </a>\r\n')
            __M_writer('   </div>\r\n')
        else:
            __M_writer('    <div class="content">\r\n     <p class="homeparg"><span style="font-size:40px; font-weight: bold;">Welcome to STOP.gov! </span>This online portal will help government agencies and providers work together to decrease America\'s opiod epidemic. Login to start today!</p>\r\n     <br><hr><br>\r\n     <p style="text-align:center;font-family:century gothic; font-size:36px;">I am a:</p>\r\n     <a href="/account/login/1/" class="alinkbox">\r\n     <div class="linkbox prov">\r\n        <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/avatar.png">\r\n        <p class="prov">Prescriber</p>\r\n     </div>\r\n    </a>\r\n    <a href="/account/login/2/" class="alinkbox">\r\n     <div class="linkbox gov">\r\n        <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/heart.png">\r\n        <p class="gov">Health Official</p>\r\n     </div>\r\n    </a>\r\n     <a href="/account/login/3/" class="alinkbox">\r\n     <div class="linkbox hha">\r\n        <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/HHA.png">\r\n        <p class="hha">HHA Clerk</p>\r\n     </div>\r\n    </a>\r\n   \r\n<br>\r\n<hr>\r\n\r\n    </div>\r\n')
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
{"filename": "C:/Users/Isaac/intexsite/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "47": 1, "52": 3, "57": 7, "62": 11, "67": 91, "77": 3, "83": 3, "89": 5, "95": 5, "101": 9, "107": 9, "113": 13, "122": 13, "123": 14, "124": 15, "125": 17, "126": 18, "127": 20, "128": 20, "129": 26, "130": 26, "131": 31, "132": 32, "133": 34, "134": 34, "135": 40, "136": 40, "137": 45, "138": 46, "139": 48, "140": 48, "141": 53, "142": 54, "143": 56, "144": 56, "145": 61, "146": 62, "147": 63, "148": 69, "149": 69, "150": 75, "151": 75, "152": 81, "153": 81, "159": 93, "165": 93, "171": 165}}
__M_END_METADATA
"""
