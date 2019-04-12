# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555046345.3313053
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
        self = context.get('self', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def bodclass():
            return render_bodclass(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
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
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.is_authenticated:
            __M_writer('   <div class="content">\r\n         <p class="homeparg"><span style="font-size:40px; font-weight: bold;">Welcome to STOP.gov! </span>This online portal will help government agencies and providers work together to decrease America\'s opiod epidemic. Let\'s start fixing today!</p>  \r\n         <br><hr><br>\r\n')
            if request.user.has_perm('account.search') or request.user.has_perm('account.safesearch'):
                __M_writer('         <a href="/portal/search/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/pill3.png">\r\n               <p class="hha">Search Drugs</p>\r\n            </div>\r\n           </a>\r\n           <a href="/portal/search/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/people.png">\r\n               <p style="color:#33BDA6">Search Providers</p>\r\n            </div>\r\n           </a>\r\n')
            if request.user.has_perm('account.analytics'):
                __M_writer('         <a href="/portal/analytics/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/analytics.png">\r\n               <p style="color:#8BD6F6">View Analytics</p>\r\n            </div>\r\n           </a>\r\n')
            if request.user.has_perm('account.CRUD'):
                __M_writer('         <a href="/portal/listings/" class="alinkbox">\r\n            <div class="linkbox hha" style="margin-left:10%;width:100vw;max-width: 800px">\r\n               <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/listing.png">\r\n               <p style="color:#FC5936">Edit Listings</p>\r\n            </div>\r\n           </a>\r\n')
            __M_writer('         <br><hr><br>\r\n   </div>\r\n')
        else:
            __M_writer('<div class="content">\r\n     <p class="homeparg"><span style="font-size:40px; font-weight: bold;">Welcome to STOP.gov! </span>This online portal will help government agencies and providers work together to decrease America\'s opiod epidemic. Login to start today!</p>\r\n     <br><hr><br>\r\n     <input class="log-btn doc-btn" type="checkbox" id="doclogbtn" />\r\n     <input class="log-btn off-btn" type="checkbox" id="offlogbtn" />\r\n     <input class="log-btn hha-btn" type="checkbox" id="hhalogbtn" />\r\n\r\n         <div id="logoptions">\r\n            <p style="text-align:center;font-family:century gothic; font-size:36px;">I am a:</p>\r\n               <label class="alinkbox" for="doclogbtn">\r\n               <div class="linkbox prov " style="margin-left:200px;">\r\n                  <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/avatar.png">\r\n                  <p class="prov">Prescriber</p>\r\n               </div>\r\n               </label>\r\n            <label class="alinkbox" for="offlogbtn">\r\n               <div class="linkbox gov" style="margin-left:200px;">\r\n                  <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/heart.png">\r\n                  <p class="gov">Health Official</p>\r\n               </div>\r\n            </label>\r\n            <label class="alinkbox" for="hhalogbtn">\r\n               <div class="linkbox hha" style="margin-left:200px;">\r\n                  <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/HHA.png">\r\n                  <p class="hha">HHA Clerk</p>\r\n               </div>\r\n            </label>\r\n         </div>\r\n         <div class="doclog"style="align-content:center;">\r\n               <p style="text-align:center;font-family:century gothic; font-size:36px;">I am a:</p>\r\n               <div class="linkbox doc" style="padding-left: 80px;">\r\n                  <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/avatar.png">\r\n                  <p class="prov">Prescriber</p>\r\n                  <form action="" method="post">\r\n                        <table class="formlabel">\r\n                        ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form ))
            __M_writer('\r\n                        </table>\r\n                        <p style="margin-left:40%; margin-top:15px;"><input type="submit" class="btn mybtn" value="Login"/></p>\r\n                  </form>\r\n                  <label for="doclogbtn"><p>I\'m not a prescriber</p></label>\r\n               </div>\r\n         </div>\r\n         <div class="offlog" style="align-content:center;">\r\n               <p style="text-align:center;font-family:century gothic; font-size:36px;">I am a:</p>\r\n               <div class="linkbox off" style="padding-left: 50px;">\r\n                  <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/heart.png">\r\n                  <p class="gov" style="font-size:52px;">Health Official</p>\r\n                  <br><br>\r\n                  <form action="" method="post">\r\n                        <table class="formlabel">\r\n                        ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form ))
            __M_writer('\r\n                        </table>\r\n                        <p style="margin-left:40%; margin-top:15px;"><input type="submit" class="btn mybtn" value="Login"/></p>\r\n                  </form>\r\n                  <label for="offlogbtn"><p>I\'m not a health official</p></label>\r\n               </div>\r\n         </div>\r\n         <div class="hhalog" style="align-content:center;">\r\n               <p style="text-align:center;font-family:century gothic; font-size:36px;">I am a:</p>\r\n               <div class="linkbox off" style="padding-left: 50px;">\r\n                  <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/HHA.png">\r\n                  <p class="hha" style="font-size:52px;">HHA Clerk</p>\r\n                  <br><br>\r\n                  <form action="" method="post">\r\n                        <table class="formlabel">\r\n                        ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( form ))
            __M_writer('\r\n                        </table>\r\n                        <p style="margin-left:40%; margin-top:15px;"><input type="submit" class="btn mybtn" value="Login"/></p>\r\n                  </form>\r\n                  <label for="hhalogbtn"><p>I\'m not a HHA data clerk</p></label>\r\n               </div>\r\n         </div>\r\n      <br>\r\n      <hr>\r\n    </div>\r\n')
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
{"filename": "C:/Users/Isaac/intexsite/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "48": 1, "53": 3, "58": 7, "63": 11, "68": 127, "78": 3, "84": 3, "90": 5, "96": 5, "102": 9, "108": 9, "114": 13, "124": 13, "125": 14, "126": 15, "127": 18, "128": 19, "129": 21, "130": 21, "131": 27, "132": 27, "133": 32, "134": 33, "135": 35, "136": 35, "137": 40, "138": 41, "139": 43, "140": 43, "141": 48, "142": 50, "143": 51, "144": 62, "145": 62, "146": 68, "147": 68, "148": 74, "149": 74, "150": 82, "151": 82, "152": 86, "153": 86, "154": 96, "155": 96, "156": 101, "157": 101, "158": 111, "159": 111, "160": 116, "161": 116, "167": 129, "173": 129, "179": 173}}
__M_END_METADATA
"""
