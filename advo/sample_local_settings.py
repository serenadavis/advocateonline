DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'advocate',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost'
    }
}

STRIPE_SUBSCRIBE_SECRET_KEY = "XXXX"
STRIPE_DONATE_SECRET_KEY = "XXXX"