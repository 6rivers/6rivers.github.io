AUTHOR = 'Ranganath S'
SITENAME = "Ranganath S"
SITEURL = 'https://ranganaths.com'
THEME = 'themes/alchemy'
SITESUBTITLE = 'Jottings on tech and life'


PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing


HIDE_AUTHORS = True

ICONS = [('twitter', 'https://twitter.com/imRanganathS')]



# Blogroll
#LINKS = (
#    ('Twitter', 'http://getpelican.com/'),
#    ('Python.org', 'http://python.org/'),
#    ('Jinja2', 'http://jinja.pocoo.org/'),
#)

# Social widget
#SOCIAL = (('Twitter', 'https://twitter.com/imRanganathS'))

DEFAULT_PAGINATION = 10

#THEME = r"C:\Users\ranganath\Desktop\Coding\Blogsite\Theme\alchemy\alchemy"
#BOOTSTRAP_CSS = r"C:\Users\ranganath\Desktop\Coding\Blogsite\Theme\alchemy\alchemy\static\css\bootstrap.min.css"
THEME_CSS_OVERRIDES = ['theme/css/theme1.css']   # 'theme/ is given in the documentation of alchemy'
#HOME_COVER = 'https://casper.ghost.org/v1.0.0/images/welcome.jpg'

STATIC_PATHS = ['extras', 'images', 'extras/CNAME']
EXTRA_PATH_METADATA = {
    'extras/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extras/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'extras/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extras/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extras/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/site.webmanifest': {'path': 'site.webmanifest'},
    'extras/mstile-150x150.png': {'path': 'mstile-150x150.png'},
    'extras/mstile-70x70.png': {'path': 'mstile-70x70.png'},
    'extras/mstile-310x310.png': {'path': 'mstile-310x310.png'},
    'extras/mstile-144x144.png': {'path': 'mstile-144x144.png'},
    'extras/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'},
    'extras/CNAME': {'path': 'CNAME'}
}

RFG_FAVICONS = True

SITEIMAGE = 'images/logo.svg width=200 height=160'
SITEIMAGE1 = 'images/avatar.png width=80 height=50'


#BOOTSTRAP_CSS = r"C:\Users\ranganath\Desktop\Coding\Blogsite\Theme\alchemy\alchemy\static\css" 

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME   = True
DISPLAY_MENU   = True



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True