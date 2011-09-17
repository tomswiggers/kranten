import os

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

from django.db import models
from django.core.management import call_command
from newspaper.models import *

call_command('syncdb')
