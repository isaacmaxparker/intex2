# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1554837714.6301215
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
        def left_content():
            return render_left_content(context._locals(__M_locals))
        def middleclass():
            return render_middleclass(context._locals(__M_locals))
        def right_content():
            return render_right_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def page_title():
            return render_page_title(context._locals(__M_locals))
        def site_content():
            return render_site_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        user = context.get('user', UNDEFINED)
        def bodyclass():
            return render_bodyclass(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def navbar_items():
            return render_navbar_items(context._locals(__M_locals))
        def logo():
            return render_logo(context._locals(__M_locals))
        def page_header_title():
            return render_page_header_title(context._locals(__M_locals))
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
                __M_writer(' presnav"  href="/portal/search/">Search</a>\r\n                                </li>    \r\n')
            if user.groups.filter(name='HealthOfficials').exists():
                __M_writer('                                <li class="mynav-item">\r\n                                        <a class="navtitle offtext">Health Official Tools:</a>\r\n                                </li>\r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='search' else ' '))
                __M_writer(' offnav" data-toggle="tab" href="/portal/search/">Search</a>\r\n                                </li>  \r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='analytics' else ' '))
                __M_writer(' offnav" data-toggle="tab" href="/portal/analytics/">Analytics</a>\r\n                                </li> \r\n')
            if user.groups.filter(name='HHS').exists():
                __M_writer('                                <li class="mynav-item">\r\n                                        <a class="navtitle hhatext">Data Clerk Tools:</a>\r\n                                </li>\r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='search' else ' '))
                __M_writer(' hhanav" data-toggle="tab" href="/portal/search/">Search</a>\r\n                                </li> \r\n                                <li class="nav-item mynav-item">\r\n                                        <a class="nav-link ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( 'active' if request.dmp.page =='search' else ' '))
                __M_writer(' hhanav" data-toggle="tab" href="/portal/edit/">Edit Listings</a>\r\n                                </li>   \r\n')
        __M_writer('                           \r\n                            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navbar_items'):
            context['self'].navbar_items(**pageargs)
        

        __M_writer('\r\n                            \r\n')
        if request.user.is_authenticated:
            if user.groups.filter(name='Prescribers').exists():
                __M_writer('                                <li class="nav-item dropdown mynav-item" style="float:right; position: absolute; right: 0; margin-right:10;">\r\n                                    <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                __M_writer('homepage/media/UserImages/')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
                __M_writer('.png" class="loginimg">\r\n                                    <a class="nav-link dropdown-toggle" style="color:rgb(3, 137, 150);" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                                      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hello, ')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
                __M_writer(' \r\n                                    </a> \r\n                                    <div class="dropdown-menu docdropdown " aria-labelledby="navbarDropdown">\r\n                                        <a class="dropdown-item" style="color:black;" href="/account/index">Account</a>\r\n                                        <a class="dropdown-item" style="color:black;" href="/account/logout">Logout</a>\r\n                                    </div>\r\n                                </li>\r\n')
            else:
                if user.groups.filter(name='HealthOfficials').exists():  
                    __M_writer('                                        <li class="nav-item dropdown mynav-item" style="float:right; position: absolute; right: 0; margin-right:10;">\r\n                                            <img src="')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                    __M_writer('homepage/media/UserImages/')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
                    __M_writer('.png" class="loginimg">\r\n                                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hello, ')
                    __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
                    __M_writer(' \r\n                                            </a> \r\n                                            <div class="dropdown-menu offdropdown" aria-labelledby="navbarDropdown">\r\n                                                <a class="dropdown-item " style="color:black;"  href="/account/index">Account</a>\r\n                                                <a class="dropdown-item" style="color:black;" href="/account/logout">Logout</a>\r\n                                            </div>\r\n                                        </li>\r\n')
                else:
                    if user.groups.filter(name='HHS').exists():
                        __M_writer('                                            <li class="nav-item dropdown mynav-item" style="float:right; position: absolute; right: 0; margin-right:10; border-color:#EFC849!important;">\r\n                                                <img src="')
                        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                        __M_writer('homepage/media/UserImages/')
                        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
                        __M_writer('.png" class="loginimg">\r\n                                                <a class="nav-link dropdown-toggle" style="color:rgb(145, 112, 5); padding-top:10px;" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hello, ')
                        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
                        __M_writer(' \r\n                                                </a> \r\n                                                <div class="dropdown-menu hhadropdown " aria-labelledby="navbarDropdown">\r\n                                                    <a class="dropdown-item" style="color:black;" href="/account/index">Account</a>\r\n                                                    <a class="dropdown-item" style="color:black;" href="/account/logout">Logout</a>\r\n                                                </div>\r\n                                            </li>\r\n')
                    else:
                        __M_writer('                                            <li class="nav-item dropdown mynav-item" style="float:right; position: absolute; right: 0; margin-right:10;">\r\n                                                <img src="')
                        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
                        __M_writer('homepage/media/UserImages/')
                        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
                        __M_writer('.png" class="loginimg">\r\n                                                <a class="nav-link dropdown-toggle" style="color:#4B93FF;" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                                                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hello, ')
                        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
                        __M_writer(' \r\n                                                </a> \r\n                                                <div class="dropdown-menu mydropdown " aria-labelledby="navbarDropdown">\r\n                                                    <a class="dropdown-item" style="color:black;" href="/account/index">Account</a>\r\n                                                    <a class="dropdown-item" style="color:black;" href="/account/logout">Logout</a>\r\n                                                </div>\r\n                                            </li>\r\n')
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
        

        __M_writer('\r\n</div>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'middleclass'):
            context['self'].middleclass(**pageargs)
        

        __M_writer('\r\n    ')
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
        self = context.get('self', UNDEFINED)
        def logo():
            return render_logo(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if user.groups.filter(name='Prescribers').exists():
            __M_writer('                <img src="')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
            __M_writer('homepage/media/avatar.png" alt="python"  class="logo2"/>\r\n')
        else:
            if user.groups.filter(name='HealthOfficials').exists():
                __M_writer('                    <img src="')
                __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
                __M_writer('homepage/media/heart.png" alt="python" class="logo2" />\r\n')
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
{"filename": "C:/Users/Isaac/intexsite/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 186, "20": 0, "47": 2, "52": 12, "53": 17, "54": 17, "55": 17, "56": 19, "57": 19, "58": 20, "59": 20, "60": 25, "61": 25, "62": 27, "63": 28, "64": 28, "65": 29, "66": 29, "71": 34, "76": 54, "77": 59, "78": 59, "79": 62, "80": 62, "81": 65, "82": 65, "83": 67, "84": 68, "85": 69, "86": 73, "87": 73, "88": 76, "89": 77, "90": 81, "91": 81, "92": 84, "93": 84, "94": 87, "95": 88, "96": 92, "97": 92, "98": 95, "99": 95, "100": 99, "105": 102, "106": 104, "107": 105, "108": 106, "109": 107, "110": 107, "111": 107, "112": 107, "113": 109, "114": 109, "115": 116, "116": 117, "117": 118, "118": 119, "119": 119, "120": 119, "121": 119, "122": 121, "123": 121, "124": 128, "125": 129, "126": 130, "127": 131, "128": 131, "129": 131, "130": 131, "131": 133, "132": 133, "133": 140, "134": 141, "135": 142, "136": 142, "137": 142, "138": 142, "139": 144, "140": 144, "141": 154, "142": 155, "143": 155, "144": 155, "145": 157, "150": 167, "155": 172, "160": 175, "165": 176, "170": 180, "171": 186, "172": 188, "173": 188, "179": 10, "185": 10, "191": 32, "197": 32, "203": 37, "212": 37, "213": 38, "214": 39, "215": 39, "216": 39, "217": 40, "218": 41, "219": 42, "220": 42, "221": 42, "222": 43, "223": 44, "224": 45, "225": 45, "226": 45, "227": 46, "228": 47, "229": 47, "230": 47, "231": 49, "232": 52, "238": 100, "244": 100, "250": 165, "256": 165, "262": 172, "268": 172, "274": 174, "280": 174, "286": 176, "292": 176, "298": 180, "304": 180, "310": 304}}
__M_END_METADATA
"""
