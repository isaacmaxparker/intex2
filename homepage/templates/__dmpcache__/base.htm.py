# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554771409.075599
_enable_loop = True
_template_filename = 'C:/Users/Isaac/intexsite/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['page_title', 'logo', 'navbar_items', 'page_header_title', 'left_content', 'site_content', 'right_content']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def logo():
            return render_logo(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_content():
            return render_site_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n<meta charset="UTF-8">\r\n\r\n<head>\r\n\r\n    <title>\r\n        STOP &mdash;\r\n        ')
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
        __M_writer('homepage/media/favicon.ico">\r\n\r\n    </head>\r\n    <body class="body">\r\n        <header>\r\n            <a href="/">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'logo'):
            context['self'].logo(**pageargs)
        

        __M_writer('\r\n            </a>\r\n            <nav class="mynav navbar">\r\n                <ul class="nav nav-tabs">\r\n                        <li class="mynav-item">\r\n                                <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='' else ' '))
        __M_writer('"  href="/">Home</a>\r\n                        </li>\r\n                        <li class="mynav-item">\r\n                                <a class="nav-link ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='contact' else ' '))
        __M_writer('" href="/contact/">Contact</a>\r\n                        </li> \r\n')
        if request.user.is_authenticated:
            if user.groups.filter(name='Prescribers').exists():
                __M_writer('                                <li class="mynav-item">\r\n                                        <a class="navtitle prestext">Prescriber Tools:</a>\r\n                                </li>\r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='search' else ' '))
                __M_writer(' presnav" data-toggle="tab" href="/prescriber/search">Search</a>\r\n                                </li>    \r\n')
            if user.groups.filter(name='HealthOfficials').exists():
                __M_writer('                                <li class="mynav-item">\r\n                                        <a class="navtitle offtext">Health Official Tools:</a>\r\n                                </li>\r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='search' else ' '))
                __M_writer(' offnav" data-toggle="tab" href="/prescriber/search">Search</a>\r\n                                </li>  \r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='analytics' else ' '))
                __M_writer(' offnav" data-toggle="tab" href="/prescriber/search">Analytics</a>\r\n                                </li> \r\n')
            if user.groups.filter(name='HHS').exists():
                __M_writer('                                <li class="mynav-item">\r\n                                        <a class="navtitle hhatext">Data Clerk Tools:</a>\r\n                                </li>\r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='search' else ' '))
                __M_writer(' hhanav" data-toggle="tab" href="/prescriber/search">Search</a>\r\n                                </li> \r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='search' else ' '))
                __M_writer(' hhanav" data-toggle="tab" href="/prescriber/search">Edit Listings</a>\r\n                                </li>   \r\n')
        else:
            __M_writer('                            <li class="mynav-item">\r\n                                    <a class="nav-link ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='' else ' '))
            __M_writer('"  href="/">Home</a>\r\n                            </li>\r\n                            <li class="mynav-item">\r\n                                    <a class="nav-link ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='contact' else ' '))
            __M_writer('" href="/contact/">Contact</a>\r\n                            </li> \r\n')
        __M_writer('                           \r\n                            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n                            \r\n')
        if request.user.is_authenticated:
            __M_writer('                                <li class="nav-item dropdown mynav-item" style="float:right; position: absolute; right: 0; margin-right:10;">\r\n                                    <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
            __M_writer('homepage/media/UserImages/')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
            __M_writer('.png" class="loginimg">\r\n                                    <a class="nav-link dropdown-toggle" style="color:#4B93FF;" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                                      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hello, ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
            __M_writer(' \r\n                                    </a> \r\n                                    <div class="dropdown-menu mydropdown " aria-labelledby="navbarDropdown">\r\n                                        <a class="dropdown-item mydropddownitem" href="/account/index">Account</a>\r\n                                        <a class="dropdown-item" href="/account/logout">Logout</a>\r\n                                    </div>\r\n                                </li>        \r\n')
        else:
            __M_writer('                                <li class="nav-item mynav-item" style="float:right; position: absolute; right: 0;"><a class="nav-link ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='login' else ' '))
            __M_writer('"" href="/account/login/4/" style="color:#085c49">Log In</a></li>\r\n')
        __M_writer('\r\n                           \r\n                                \r\n\r\n\r\n                 </ul>\r\n        \r\n            </nav>\r\n            <div class="title">')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'page_header_title'):
            context['self'].page_header_title(**pageargs)
        

        __M_writer('</div>\r\n        </header>\r\n\r\n        <main>\r\n<div id="site_left" class="">\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n</div>\r\n\r\n<div class="site_middle">\r\n    ')
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


def render_logo(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def logo():
            return render_logo(context)
        user = context.get('user', UNDEFINED)
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if user.groups.filter(name='Prescribers').exists():
            __M_writer('                <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
            __M_writer('homepage/media/avatar.png" alt="python" />\r\n')
        else:
            if user.groups.filter(name='HealthOfficials').exists():
                __M_writer('                    <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
                __M_writer('homepage/media/heart.png" alt="python" />\r\n')
            else:
                if user.groups.filter(name='HHS').exists():
                    __M_writer('                        <img src="')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
                    __M_writer('homepage/media/hha.png" alt="python" />\r\n')
                else:
                    __M_writer('                        <img src="')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
                    __M_writer('homepage/media/logo2.png" alt="python" />\r\n')
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
{"filename": "C:/Users/Isaac/intexsite/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"18": 149, "20": 0, "43": 2, "48": 12, "49": 17, "50": 17, "51": 17, "52": 19, "53": 19, "54": 20, "55": 20, "56": 25, "57": 25, "58": 27, "59": 28, "60": 28, "61": 29, "62": 29, "67": 52, "68": 57, "69": 57, "70": 60, "71": 60, "72": 62, "73": 63, "74": 64, "75": 68, "76": 68, "77": 71, "78": 72, "79": 76, "80": 76, "81": 79, "82": 79, "83": 82, "84": 83, "85": 87, "86": 87, "87": 90, "88": 90, "89": 93, "90": 94, "91": 95, "92": 95, "93": 98, "94": 98, "95": 101, "100": 104, "101": 106, "102": 107, "103": 108, "104": 108, "105": 108, "106": 108, "107": 110, "108": 110, "109": 117, "110": 118, "111": 118, "112": 118, "113": 120, "118": 130, "123": 135, "128": 139, "133": 143, "134": 149, "135": 151, "136": 151, "142": 10, "148": 10, "154": 35, "163": 35, "164": 36, "165": 37, "166": 37, "167": 37, "168": 38, "169": 39, "170": 40, "171": 40, "172": 40, "173": 41, "174": 42, "175": 43, "176": 43, "177": 43, "178": 44, "179": 45, "180": 45, "181": 45, "182": 47, "183": 50, "189": 102, "195": 102, "201": 128, "207": 128, "213": 135, "219": 135, "225": 139, "231": 139, "237": 143, "243": 143, "249": 243}}
__M_END_METADATA
"""
