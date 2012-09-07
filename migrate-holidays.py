from dbfpy import dbf
import os, sys
 
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

from django.db import models
from django.core.management import call_command

from newspaper.models import Holiday

def saveHoliday(clientId, begin, end):
  print 'Save Holiday: %d %s %s' % (clientId, begin, end)
  
  holiday = Holiday()
  holiday.client_id = clientId
  holiday.begindate = begin
  holiday.enddate = end

  holiday.save()


db = dbf.Dbf("migrate/KR_KLANT.DBF")

for client in db:

  if type(client['VL1VAN']).__name__ == 'date' and type(client['VL1TOT']).__name__ == 'date':
    saveHoliday(client['KLANT'], client['VL1VAN'], client['VL1TOT'])
  
  if type(client['VL2VAN']).__name__ == 'date' and type(client['VL2TOT']).__name__ == 'date':
    saveHoliday(client['KLANT'], client['VL2VAN'], client['VL2TOT'])
