from nedsoft.settings import *
import dj_database_url

DEBUG = False

TEMPLATE_DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j)oz5ddmeaftq+o5b)vywqmnogtw_6-)$z06xb$u&3k%&@iajm'

ALLOWED_HOSTS = ['nedsoft.herokuapp.com']

DATABASES['default'] = dj_database_url.config()

#Amazone s3 credentials

#Amazone bucket name
AWS_STORAGE_BUCKET_NAME = 'nedsoft-admin'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'nedsoft/static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'nedsoft.storage_backends.MediaStorage'
