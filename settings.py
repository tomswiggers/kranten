from config import Config

DATABASES = {
    'default': {
        'ENGINE': Config.dbEngine,
        'NAME': Config.dbName,                      
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.

    }
}

INSTALLED_APPS = (
  'newspaper'
)
