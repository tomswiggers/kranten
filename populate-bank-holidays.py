from dbfpy import dbf
import os, sys
 
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

from django.db import models
from django.core.management import call_command

from newspaper.models import BankHoliday

def saveBankHoliday(entrydate):
  print 'Save Bank Holiday: %s' % (entrydate)
  
  holiday = BankHoliday()
  holiday.entrydate = entrydate

  holiday.save()

saveBankHoliday('2012-01-01')
saveBankHoliday('2012-08-15')
