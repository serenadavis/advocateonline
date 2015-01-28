DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'advocate',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost'
    }
}

STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY", "XXXX") # get from a member of the tech team