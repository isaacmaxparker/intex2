# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550804776.091269
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/homepage/templates/test.htm'
_template_uri = '/homepage/templates/test.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['title', 'menu', 'site_center', 'site_left', 'site_right']


from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def site_center():
            return render_site_center(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def menu():
            return render_menu(context._locals(__M_locals))
        def site_right():
            return render_site_right(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def site_left():
            return render_site_left(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n    <meta charset="UTF-8">\r\n    <head>\r\n      \r\n        <title>Sprint 2 &mdash; ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('</title>\r\n')
        __M_writer('        <script src="/homepage/media/jquery-3.3.1.js"></script>\r\n        <link href="/homepage/media/css/bootstrap.min.css" rel="Stylesheet" type="text/css">\r\n        <script src="/homepage/media/js/bootstrap.min.js"></script>\r\n        <link rel="icon" href="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( STATIC_URL ))
        __M_writer('homepage/media/python.png">\r\n        \r\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n        ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( django_mako_plus.links(self) ))
        __M_writer('\r\n    </head>\r\n    <body>\r\n        <div class="alert alert-danger" role="alert" id="alertMessage">\r\n            Site will be down tonight due to maintenance \r\n        </div>\r\n        <header id="header"> \r\n')
        __M_writer('        </header>\r\n        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">\r\n                \r\n                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">\r\n                    <span class="navbar-toggler-icon"></span>\r\n                </button>\r\n    <div class="collapse navbar-collapse justify-content-end" id="navbarSupportedContent">\r\n        <div class="nav-item navbar-left"><img style="padding-left: 10px; padding-right: 10px;"src="')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)(STATIC_URL))
        __M_writer('homepage/media/thumbnail.png"/></div>\r\n        <ul class="navbar-nav mr-4">\r\n            \r\n            \r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\r\n            \r\n')
        if request.user.is_authenticated: 
            __M_writer('            <li class="nav-item dropdown">\r\n                <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">\r\n                    Welcome, ')
            __M_writer(django_mako_plus.ExpressionPostProcessor(self)(request.user.username))
            __M_writer('\r\n                </a>\r\n                <div class="dropdown-menu" aria-labelledby="navbarDropdown">\r\n                    <a class="dropdown-item" href="/account/index">Account</a>\r\n                <div class="dropdown-divider"></div>\r\n                    <a class="dropdown-item" href="/account/logout">Logout</a>\r\n                </div>\r\n            </li>\r\n')
        else:
            __M_writer('            <li class="nav-item"><a class="nav-link" href="/account/login">Log In</a></li>\r\n')
        __M_writer('            \r\n               \r\n        </ul>\r\n            \r\n        </div>\r\n    </nav>\r\n        \r\n        \r\n        <main>\r\n            <div id="site_center">\r\n                ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_center'):
            context['self'].site_center(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            \r\n            <div id="site_left">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_left'):
            context['self'].site_left(**pageargs)
        

        __M_writer('\r\n            </div>\r\n            <div id="site_right">\r\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_right'):
            context['self'].site_right(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </main>\r\n        <footer>\r\n            \r\n            ')
        __M_writer('\r\n            <div class="center">\r\n                &copy; ')
        __M_writer(django_mako_plus.ExpressionPostProcessor(self)( datetime.today().year ))
        __M_writer('\r\n            </div>\r\n        </footer>\r\n    </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu():
            return render_menu(context)
        __M_writer = context.writer()
        __M_writer(' \r\n                \r\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_center():
            return render_site_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n                    \r\n                ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_left():
            return render_site_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n                        \r\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_right():
            return render_site_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n                        \r\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/homepage/templates/test.htm", "uri": "/homepage/templates/test.htm", "source_encoding": "utf-8", "line_map": {"18": 80, "20": 0, "38": 1, "43": 6, "44": 8, "45": 11, "46": 11, "47": 14, "48": 15, "49": 15, "50": 23, "51": 30, "52": 30, "57": 36, "58": 38, "59": 39, "60": 41, "61": 41, "62": 49, "63": 50, "64": 52, "69": 64, "74": 70, "79": 75, "80": 80, "81": 82, "82": 82, "88": 6, "99": 34, "105": 34, "111": 62, "117": 62, "123": 68, "129": 68, "135": 73, "141": 73, "147": 141}}
__M_END_METADATA
"""
