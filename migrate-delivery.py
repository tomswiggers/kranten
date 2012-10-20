from dbfpy import dbf
import os, sys
 
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

from django.db import models
from django.core.management import call_command

from newspaper.models import Delivery
from newspaper.models import Item

import datetime

def saveDelivery(delivery):
  item = Item()
  deliveryObj = Delivery()

  deliveryObj.begindate = getDate(delivery['DATVAN'], 2000, 1, 1)
  deliveryObj.enddate = getDate(delivery['DATTOT'], 2999, 12, 31)
  deliveryObj.item_id = item.getItemIdByName(delivery['DIENST'])
  deliveryObj.client_id = delivery['KLANT']
  deliveryObj.days = getDays(delivery)

  deliveryObj.save()

  print deliveryObj

def getDate(entrydate, year, month, day):
  if type(entrydate).__name__ == 'date':
    return entrydate
  else:
    return datetime.date(year, month, day)

def getDays(delivery):
  days = 0

  for i in range(2, 7):
    
    if delivery['LEV' + str(i)] == 'Y':
      days = days + Item().getDayBit(i-2)

  return days

db = dbf.Dbf("migrate/LEVER.DBF")

print "Migrate delivery"
print "================"

for rec in db:
  saveDelivery(rec)
