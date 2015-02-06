DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'advocate',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost'
    }
}

STRIPE_BUY_SECRET_KEY = "XXXX"
STRIPE_DONATE_SECRET_KEY = "XXXX"