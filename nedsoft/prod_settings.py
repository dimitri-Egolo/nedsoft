from nedsoft.settings import *
import dj_database_url

DEBUG = False

TEMPLATE_DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j)oz5ddmeaftq+o5b)vywqmnogtw_6-)$z06xb$u&3k%&@iajm'

ALLOWED_HOSTS = ['nedsoft.herokuapp.com']

DATABASES['default'] = dj_database_url.config()
