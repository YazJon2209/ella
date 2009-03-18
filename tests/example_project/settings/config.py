from tempfile import gettempdir
from os.path import join, dirname

import example_project

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DISABLE_CACHE_TEMPLATE = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = join(gettempdir(), 'ella_example_project.db')
TEST_DATABASE_NAME =join(gettempdir(), 'test_ella_example_project.db')
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = 'Europe/Prague'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1
USE_I18N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = '88b-01f^x4lh$-s5-hdccnicekg07)niir2g6)93!0#k(=mfv$'

# TODO: Fix logging
# init logger
#LOGGING_CONFIG_FILE = join(dirname(testbed.__file__), 'settings', 'logger.ini')
#if isinstance(LOGGING_CONFIG_FILE, basestring) and isfile(LOGGING_CONFIG_FILE):
#    logging.config.fileConfig(LOGGING_CONFIG_FILE)

# we want to reset whole cache in test
# until we do that, don't use cache
CACHE_BACKEND = 'dummy://'

# session expire
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# disable double render in admin
DOUBLE_RENDER = False

MEDIA_ROOT = join(dirname(example_project.__file__), 'static')

MEDIA_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin_media/'
NEWMAN_MEDIA_PREFIX = '/static/newman_media/'
