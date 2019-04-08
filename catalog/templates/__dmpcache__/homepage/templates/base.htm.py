# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554758162.2404363
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'bodclass', 'logo', 'navbar_items', 'page_header_title', 'left_content', 'site_content', 'right_content']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def bodclass():
            return render_bodclass(context._locals(__M_locals))
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def logo():
            return render_logo(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n<meta charset="UTF-8">\r\n\r\n<head>\r\n\r\n    <title>\r\n        Isaac\'s Hot\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_title'):
            context['self'].page_title(**pageargs)
        

        __M_writer('\r\n        </title>\r\n\r\n \r\n')
        __M_writer('        <!-- <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage\\media\\jquery.js"></script> -->\r\n        <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n        <script src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/js/bootstrap.min.js"></script>\r\n        <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/css/bootstrap.min.css" rel="stylesheet" type="text/css">\r\n        <!-- <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>\r\n        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>\r\n        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script> -->\r\n         \r\n         <link rel="stylesheet" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/styles/base.scss">\r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/favicon.ico">\r\n\r\n    </head>\r\n    <body ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodclass'):
            context['self'].bodclass(**pageargs)
        

        __M_writer(' </body>\r\n        <header>\r\n            <a href="/">')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'logo'):
            context['self'].logo(**pageargs)
        

        __M_writer('</a>\r\n            <nav class="mynav navbar">\r\n                <ul class="nav nav-tabs">\r\n                    \r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n                    \r\n')
        if request.user.is_authenticated:
            __M_writer('                                <li class="nav-item dropdown mynav-item" style="float:right; position: absolute; right: 0; margin-right:10;">\r\n                                    <a class="nav-link dropdown-toggle" style="color:#085c49;" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                                       &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Hello, ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
            __M_writer(' \r\n                                    </a> \r\n                                    <div class="dropdown-menu mydropdown " aria-labelledby="navbarDropdown">\r\n                                        <a class="dropdown-item mydropddownitem" href="/account/index">Account</a>\r\n                                    <div class="dropdown-divider"></div>\r\n                                        <a class="dropdown-item mydropddownitem" href="/catalog/cart">My Cart</a>\r\n                                    <div class="dropdown-divider"></div>\r\n                                        <a class="dropdown-item" href="/account/logout">Logout</a>\r\n                                    </div>\r\n                                </li>        \r\n')
        else:
            __M_writer('                                <li class="nav-item mynav-item" style="float:right; position: absolute; right: 0;"><a class="nav-link ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='login' else ' '))
            __M_writer('"" href="/account/login/4/" style="color:#085c49">Log In</a></li>\r\n')
        __M_writer('\r\n                           \r\n                                \r\n\r\n\r\n                 </ul>\r\n        \r\n            </nav>\r\n')
        if request.user.is_authenticated:
            __M_writer('            \r\n                <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/UserImages/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
            __M_writer('.jpg" class="loginimg" >\r\n            \r\n')
        __M_writer('            \r\n\r\n            <div class="title">')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('</div>\r\n        </header>\r\n\r\n        <main>\r\n<div id="site_left" class="">\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n</div>\r\n\r\n<div id="site_middle">\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        __M_writer('\r\n</div>\r\n\r\n<div id="site_right">\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\r\n</div>\r\n        </main>\r\n\r\n        <footer>\r\n            \r\n            ')
        __M_writer('\r\n\r\n           <p class="copy"> &copy; ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(datetime.now().strftime("%Y")))
        __M_writer(' Group 2-9</p>\r\n\r\n        </footer>\r\n\r\n        </body>\r\n\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_title():
            return render_page_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n                My Project!\r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bodclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodclass():
            return render_bodclass(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_logo(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def logo():
            return render_logo(context)
        __M_writer = context.writer()
        __M_writer('<img src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/logo2.png" alt="python" />')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_items():
            return render_navbar_items(context)
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n                            <li class="nav-item mynav-item">\r\n                                    <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='index' else ' '))
        __M_writer('" data-toggle="tab" href="/">Home</a>\r\n                                  </li>\r\n                            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_header_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def page_header_title():
            return render_page_header_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n                <p class = "hometitle">Stop the epidemic</p>\r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('Left Side')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_content():
            return render_site_content(context)
        __M_writer = context.writer()
        __M_writer('404 Error Page Content not found')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_right_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def right_content():
            return render_right_content(context)
        __M_writer = context.writer()
        __M_writer('right Side')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/intexsite/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 96, "20": 0, "44": 2, "49": 12, "50": 17, "51": 17, "52": 17, "53": 19, "54": 19, "55": 20, "56": 20, "57": 25, "58": 25, "59": 27, "60": 28, "61": 28, "62": 29, "63": 29, "68": 32, "73": 34, "78": 42, "79": 44, "80": 45, "81": 47, "82": 47, "83": 57, "84": 58, "85": 58, "86": 58, "87": 60, "88": 68, "89": 69, "90": 70, "91": 70, "92": 70, "93": 70, "94": 73, "99": 77, "104": 82, "109": 86, "114": 90, "115": 96, "116": 98, "117": 98, "123": 10, "129": 10, "135": 32, "146": 34, "154": 34, "155": 34, "156": 34, "162": 38, "170": 38, "171": 40, "172": 40, "178": 75, "184": 75, "190": 82, "196": 82, "202": 86, "208": 86, "214": 90, "220": 90, "226": 220}}
__M_END_METADATA
"""
