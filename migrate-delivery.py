from dbfpy import dbf
import os, sys
 
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

from django.db import models
from django.core.management import call_command

from newspaper.models import Delivery

import datetime

db = dbf.Dbf("migrate/LEVER.DBF")

print "Migrate delivery"
print "============="

for rec in db:
  print rec
