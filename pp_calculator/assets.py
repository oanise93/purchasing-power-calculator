# -*- coding: utf-8 -*-
"""Application assets."""
from flask_assets import Bundle, Environment

css = Bundle(
    # 'libs/bootstrap/dist/css/bootstrap.css',
    'libs/semantic/dist/semantic.css',
    'css/style.css',
    filters='cssmin',
    output='public/css/common.css'
)

js = Bundle(
    'libs/jquery/dist/jquery.js',
    # 'libs/bootstrap/dist/js/bootstrap.js',
    'libs/semantic/dist/semantic.js',
    'js/plugins.js',
    filters='jsmin',
    output='public/js/common.js'
)

assets = Environment()

assets.register('js_all', js)
assets.register('css_all', css)
