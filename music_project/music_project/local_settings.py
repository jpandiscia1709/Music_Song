

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m&=nub7*fk#@19#-msg_nm8yncflhd_hidg!6@$4qa8r33a8*4'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'music_library_database',
        'USER':'root',
        'PASSWORD':'BigBanana$',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }

    }
}
