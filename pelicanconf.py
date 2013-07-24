#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pytz import timezone
from datetime import datetime

AUTHOR = 'Dale Lukas Peterson'
SITENAME = 'Pink Noise'
SITEURL = ''

TIMEZONE = 'America/Los_Angeles'
d = datetime.utcnow()
DEFAULT_DATE = (d.year, d.month, d.day, d.hour, d.minute, d.second)
DEFAULT_DATE_FORMAT = '%Y-%m-%dT%H:%MZ'

DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'
DISPLAY_CATEGORIES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'extra/favicon.ico',
    ]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    }

THEME = 'themes/pelican-octopress'

