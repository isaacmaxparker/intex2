# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1555049535.877894
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'bodyclass', 'logo', 'navbar_items', 'page_header_title', 'left_content', 'middleclass', 'site_content', 'right_content']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        user = context.get('user', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def right_content():
            return render_right_content(context._locals(__M_locals))
        def middleclass():
            return render_middleclass(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        def logo():
            return render_logo(context._locals(__M_locals))
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n<meta charset="UTF-8">\r\n\r\n<head>\r\n\r\n    <title>\r\n        STOP.GOV\r\n        ')
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
        __M_writer('homepage/media/favicon.ico">\r\n\r\n    </head>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bodyclass'):
            context['self'].bodyclass(**pageargs)
        

        __M_writer('\r\n        <header>\r\n            <a href="/">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'logo'):
            context['self'].logo(**pageargs)
        

        __M_writer('\r\n            </a>\r\n            <nav class="mynav navbar">\r\n                <ul class="nav nav-tabs">\r\n                        <li class="mynav-item">\r\n                                <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='' else ' '))
        __M_writer('"  href="/">Home</a>\r\n                        </li>\r\n                        <li class="mynav-item">\r\n                                <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='about' else ' '))
        __M_writer('" href="/about/">About</a>\r\n                        </li> \r\n                        <li class="mynav-item">\r\n                                <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='contact' else ' '))
        __M_writer('" href="/contact/">Contact</a>\r\n                        </li> \r\n')
        if request.user.is_authenticated:
            if user.groups.filter(name='Prescribers').exists():
                __M_writer('                                <li class="mynav-item">\r\n                                        <a class="navtitle prestext">Prescriber Tools:</a>\r\n                                </li>\r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='search' else ' '))
                __M_writer(' presnav"  href="/portal/search/">Search</a>\r\n                                </li>   \r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='analytics' else ' '))
                __M_writer(' presnav" href="/portal/analytics/">Analytics</a>\r\n                                </li>\r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='account' else ' '))
                __M_writer(' presnav" href="/account//">My Account</a>\r\n                                </li>\r\n                                <li class="nav-item mynav-item">\r\n                                    <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='logout' else ' '))
                __M_writer(' presnav" href="/account/logout/">Log Out</a>  \r\n')
            if user.groups.filter(name='HealthOfficials').exists() or user.groups.filter(name='Officials').exists():
                __M_writer('                                <li class="mynav-item">\r\n                                        <a class="navtitle offtext">Health Official Tools:</a>\r\n                                </li>\r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='search' else ' '))
                __M_writer(' offnav" href="/portal/search/">Search</a>\r\n                                </li>  \r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='analytics' else ' '))
                __M_writer(' offnav" href="/portal/analytics/">Analytics</a>\r\n                                </li>\r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='account' else ' '))
                __M_writer(' offnav" href="/account/index/">My Account</a>\r\n                                </li>\r\n                                <li class="nav-item mynav-item">\r\n                                    <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='logout' else ' '))
                __M_writer(' offnav" href="/account/logout/">Log Out</a>\r\n                                </li>\r\n')
            if user.groups.filter(name='HHS').exists():
                __M_writer('                                <li class="mynav-item">\r\n                                        <a class="navtitle hhatext">Data Clerk Tools:</a>\r\n                                </li>\r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='search' else ' '))
                __M_writer(' hhanav" href="/portal/search/">Search</a>\r\n                                </li> \r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='listings' else ' '))
                __M_writer(' hhanav" href="/portal/listings/">Edit Listings</a>\r\n                                </li> \r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='account' else ' '))
                __M_writer(' hhanav" href="/account/index/">My Account</a>\r\n                                </li>  \r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='logout' else ' '))
                __M_writer(' hhanav" href="/account/logout/">Logout</a>\r\n                                </li>    \r\n')
        if request.user.is_authenticated:
            __M_writer('                           \r\n                           <p style="position:absolute;right:0;top:40;font-family: \'Trebuchet MS\';font-size: 20px;padding: 10px;color:rgba(128, 128, 128, 0.486);"><img src="/static/homepage/media/UserImages/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
            __M_writer('.png" style="width:30px;height: 30px; margin-right:200px;"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hello ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
            __M_writer('!</p>\r\n                           \r\n')
        else:
            __M_writer('                                <li class="nav-item mynav-item" style="float:right; position: absolute; right: 0;"><a class="nav-link ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='login' else ' '))
            __M_writer('"" href="/account/login/4/" style="color:#085c49">Log In</a></li>\r\n                           \r\n')
        __M_writer('                            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n                            \r\n                            \r\n\r\n                           \r\n                                \r\n\r\n\r\n                 </ul>\r\n        \r\n            </nav>\r\n            <div class="title">')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('</div>\r\n        </header>\r\n        <main>\r\n<div id="site_left" class="">\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n</div>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'middleclass'):
            context['self'].middleclass(**pageargs)
        

        __M_writer('\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        __M_writer('\r\n</div>\r\n\r\n<div id="site_right">\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'right_content'):
            context['self'].right_content(**pageargs)
        

        __M_writer('\r\n</div>\r\n        </main>\r\n\r\n        <footer>\r\n            ')
        __M_writer('\r\n            \r\n           <p class="copy"> &copy; ')
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


def render_bodyclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bodyclass():
            return render_bodyclass(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <body class="body">\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_logo(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        user = context.get('user', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def logo():
            return render_logo(context)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if user.groups.filter(name='Prescribers').exists():
            __M_writer('                <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
            __M_writer('homepage/media/avatar.png" alt="python"  class="logo2"/>\r\n')
        else:
            if user.groups.filter(name='HealthOfficials').exists() or user.groups.filter(name='Officials').exists():
                __M_writer('                    <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
                __M_writer('homepage/media/heart.png" alt="python" class="logo2" />\r\n                    \r\n')
            else:
                if user.groups.filter(name='HHS').exists():
                    __M_writer('                        <img src="')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
                    __M_writer('homepage/media/hha.png" alt="python" class="logo2" />\r\n')
                else:
                    __M_writer('                        <img src="')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
                    __M_writer('homepage/media/logo2.png" alt="python" class="logo"/>\r\n')
                __M_writer('                        \r\n')
        __M_writer('                \r\n                \r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navbar_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def navbar_items():
            return render_navbar_items(context)
        __M_writer = context.writer()
        __M_writer('\r\n                                         \r\n                            ')
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


def render_middleclass(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def middleclass():
            return render_middleclass(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="site_middle">')
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
{"filename": "C:/Users/Isaac/intexsite/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 160, "20": 0, "47": 2, "52": 12, "53": 17, "54": 17, "55": 17, "56": 19, "57": 19, "58": 20, "59": 20, "60": 25, "61": 25, "62": 27, "63": 28, "64": 28, "65": 29, "66": 29, "71": 34, "76": 55, "77": 60, "78": 60, "79": 63, "80": 63, "81": 66, "82": 66, "83": 68, "84": 69, "85": 70, "86": 74, "87": 74, "88": 77, "89": 77, "90": 80, "91": 80, "92": 83, "93": 83, "94": 85, "95": 86, "96": 90, "97": 90, "98": 93, "99": 93, "100": 96, "101": 96, "102": 99, "103": 99, "104": 102, "105": 103, "106": 107, "107": 107, "108": 110, "109": 110, "110": 113, "111": 113, "112": 116, "113": 116, "114": 120, "115": 121, "116": 122, "117": 122, "118": 122, "119": 122, "120": 124, "121": 125, "122": 125, "123": 125, "124": 128, "129": 130, "134": 143, "139": 147, "144": 150, "149": 151, "154": 155, "155": 160, "156": 162, "157": 162, "163": 10, "169": 10, "175": 32, "181": 32, "187": 37, "196": 37, "197": 38, "198": 39, "199": 39, "200": 39, "201": 40, "202": 41, "203": 42, "204": 42, "205": 42, "206": 44, "207": 45, "208": 46, "209": 46, "210": 46, "211": 47, "212": 48, "213": 48, "214": 48, "215": 50, "216": 53, "222": 128, "228": 128, "234": 141, "240": 141, "246": 147, "252": 147, "258": 149, "264": 149, "270": 151, "276": 151, "282": 155, "288": 155, "294": 288}}
__M_END_METADATA
"""
