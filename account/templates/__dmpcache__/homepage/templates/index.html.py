# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1550602831.6607268
_enable_loop = True
_template_filename = 'C:/Users/Isaac/mysite/homepage/templates/index.html'
_template_uri = '/homepage/templates/index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django.utils.html
_exports = ['left_content', 'site_content']


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
        def left_content():
            return render_left_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'left_content'):
            context['self'].left_content(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'site_content'):
            context['self'].site_content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_left_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def left_content():
            return render_left_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n<ul class="nav nav-pills">\r\n    <li class="nav-item">\r\n      <a class="nav-link active" href="#">Active</a>\r\n    </li>\r\n    <li class="nav-item dropdown show">\r\n      <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="true">Dropdown</a>\r\n      <div class="dropdown-menu show" x-placement="bottom-start" style="position: absolute; will-change: transform; top: 0px; left: 0px; transform: translate3d(0px, 37px, 0px);">\r\n        <a class="dropdown-item" href="#">Action</a>\r\n        <a class="dropdown-item" href="#">Another action</a>\r\n        <a class="dropdown-item" href="#">Something else here</a>\r\n        <div class="dropdown-divider"></div>\r\n        <a class="dropdown-item" href="#">Separated link</a>\r\n      </div>\r\n    </li>\r\n    <li class="nav-item">\r\n      <a class="nav-link" href="#">Link</a>\r\n    </li>\r\n    <li class="nav-item">\r\n      <a class="nav-link disabled" href="#">Disabled</a>\r\n    </li>\r\n  </ul>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_site_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def site_content():
            return render_site_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h3>Welcome to my site. I make cool things. here is an example:</h3>\r\n      <p>\r\n\r\n          <iframe width="1000" height="600" src="https://www.youtube.com/embed/qIh-JV3RuSY?rel=0&amp;autoplay=1&mute=1" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\r\n\r\n      </p>\r\n      </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Isaac/mysite/homepage/templates/index.html", "uri": "/homepage/templates/index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 25, "53": 3, "59": 3, "65": 28, "71": 28, "77": 71}}
__M_END_METADATA
"""
