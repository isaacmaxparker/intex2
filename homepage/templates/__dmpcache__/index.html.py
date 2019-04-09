# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554826376.9468565
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
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def bodclass():
            return render_bodclass(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
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
        def site_content():
            return render_site_content(context)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.is_authenticated:
            __M_writer('   <div class="content">\r\n         <p class="homeparg"><span style="font-size:40px; font-weight: bold;">Welcome to STOP.gov! </span>This online portal will help government agencies and providers work together to decrease America\'s opiod epidemic. Let\'s start fixing today!</p>  \r\n         <br><hr><br>\r\n')
            if request.user.has_perm('account.search'):
                __M_writer('         <a href="/account/login/3/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/pill3.png">\r\n               <p class="hha">Search Drugs</p>\r\n            </div>\r\n           </a>\r\n           <a href="/account/login/3/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/people.png">\r\n               <p style="color:#33BDA6">Search Providers</p>\r\n            </div>\r\n           </a>\r\n')
            if request.user.has_perm('account.safesearch'):
                __M_writer('         <a href="/account/login/3/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/pill3.png">\r\n               <p class="hha">Search Drugs</p>\r\n            </div>\r\n           </a>\r\n           <a href="/account/login/3/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/people.png">\r\n               <p style="color:#33BDA6">Search Providers</p>\r\n            </div>\r\n           </a>\r\n')
            if request.user.has_perm('account.analytics'):
                __M_writer('         <a href="/account/login/3/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/analytics.png">\r\n               <p style="color:#8BD6F6">View Analytics</p>\r\n            </div>\r\n           </a>\r\n')
            if request.user.has_perm('account.CRUD'):
                __M_writer('         <a href="/account/login/3/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/listing.png">\r\n               <p style="color:#FC5936">Edit Listings</p>\r\n            </div>\r\n           </a>\r\n')
            __M_writer('         <br><hr><br>\r\n   </div>\r\n')
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
{"filename": "C:/Users/Isaac/intexsite/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "47": 1, "52": 3, "57": 7, "62": 11, "67": 93, "77": 3, "83": 3, "89": 5, "95": 5, "101": 9, "107": 9, "113": 13, "122": 13, "123": 14, "124": 15, "125": 18, "126": 19, "127": 21, "128": 21, "129": 27, "130": 27, "131": 32, "132": 33, "133": 35, "134": 35, "135": 41, "136": 41, "137": 46, "138": 47, "139": 49, "140": 49, "141": 54, "142": 55, "143": 57, "144": 57, "145": 62, "146": 64, "147": 65, "148": 71, "149": 71, "150": 77, "151": 77, "152": 83, "153": 83, "159": 95, "165": 95, "171": 165}}
__M_END_METADATA
"""
