#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Matt Dugan'
SITENAME = 'Just a blog.'
SITESUBTITLE = 'by Matt Dugan'
FEEDURL = 'http://mattdugan.github.io'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

ARTICLE_DIR = 'posts'
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TRANSLATION_FEED_ATOM = None
FEED_MAX_ITEMS = 20

THEME = 'theme/html5-dopetrope-md'
PLUGIN_PATH = 'plugins'
PLUGINS = ['pelican_youtube']

# Blogroll
LINKS = (('My Corporate Blog at Shadow-Soft', 'http://www.shadow-soft.com/blog'),
         ('Atlanta JBoss Users Group', 'http://www.meetup.com/ATL-JBUG/'),
         ('Planet Fedora Project', 'http://planet.fedoraproject.org'),
         ('Use Vim!', 'http://www.usevim.com'),
         ('Hacker News', 'https://news.ycombinator.com'),
         ('Reddit r/Linux', 'http://www.reddit.com/r/linux/'), )

# Social widget
SOCIAL = (('Google+', 'https://plus.google.com/113099432515471915221/posts'),
          ('LinkedIn', 'http://linkedin.com/in/mattdugan'),
          ('Twitter', 'https://twitter.com/dugansvoice'),
          ('GitHub', 'https://github.com/mattdugan'), )

TYPOGRIFY = True
DEFAULT_PAGINATION = 6
WITH_FUTURE_DATES = False

# Not working as desired, yet.
#PAGINATION_PATTERNS = ((1, '/', '/index.html'),
#                       (2, '/page/{number}', '/page/{number}/index.html'), )

# If not pages, then categories
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = False
OUTPUT_SOURCES = False
STATIC_PATHS = ['content/images', 'content/dwd']
OUTPUT_RETENTION = ('.git', '.gitignore')
OUTPUT_PATH = '../output/'

# Theme variables
MAIL = 'matt@intelligentgeek.com'
TWITTER_USER = 'dugansvoice'
GOOGLEPLUS_USER = '113099432515471915221'
LINKEDIN_USER = '../in/mattdugan'
ABOUT_TEXT = """
    <b>Matt Dugan</b>:<br/>
    Lead Middleware and Cloud Architect<br/>
    Technology Evangelist
    """
ABOUT_IMAGE = 'content/images/profile_photo2.png'
ABOUT_LINK = 'http://mattdugan.github.io'
COPYRIGHT = 'Matt Dugan'
SHOW_COPYRIGHT = True
