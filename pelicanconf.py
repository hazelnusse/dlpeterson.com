#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from pytz import timezone
from datetime import datetime

AUTHOR = u'Dale Lukas Peterson'
SITENAME = u'Dale Lukas Peterson'
SITESUBTITLE = u'... and some of my thoughts.'
SITEURL = ''
DISQUS_SITENAME = 'dlpeterson'

TIMEZONE = 'America/Los_Angeles'
d = datetime.utcnow()
DEFAULT_DATE = (d.year, d.month, d.day, d.hour, d.minute, d.second)
DEFAULT_DATE_FORMAT = '%Y-%m-%dT%H:%MZ'

DEFAULT_LANG = 'en'
LOCALE = 'en_US.UTF-8'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'http://github.com/hazelnusse'),
          ('google+', 'http://plus.google.com/118331842568896227320'),
          ('linkedin', 'http://www.linkedin.com/pub/dale-peterson/13/998/a3'),
          ('twitter', 'http://twitter.com/hazelnusse'),
          ('email', 'mailto:hazelnusse@gmail.com'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'extra/favicon.ico',
    ]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    }

#THEME = 'themes/pelican-octopress'
THEME = 'themes/plumage'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARTICLE_DIR = 'posts'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_DIR = 'pages'

TAGS_SAVE_AS = 'tags.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = ''
CATEGORY_URL =''# 'category/{slug}/'
CATEGORY_SAVE_AS = ''#CATEGORY_URL + 'index.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

#PAGE_URL = 'pages/{slug}'
#PAGE_SAVE_AS = 'pages/{slug}/index.html'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [("Home", "/"),
             ("About", "/about/")]

#ARCHIVES_URL = "posts/"
#ARCHIVES_SAVE_AS = "posts/index.html"
#YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'
#DAY_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/index.html'

# Deactivate author URLs
AUTHOR_SAVE_AS = False
AUTHORS_SAVE_AS = False

# Deactivate localization
ARTICLE_LANG_SAVE_AS = False
PAGE_LANG_SAVE_AS = False

