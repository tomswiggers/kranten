from dbfpy import dbf
import os, sys
 
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

from django.db import models
from django.core.management import call_command

from newspaper.models import Item
from newspaper.models import Price

import datetime

def saveItem(item):
  itemObj = Item()
  itemObj.name = item['DIENST']
  itemObj.description = unicode(item['OMSCHR'], errors='replace')
  itemObj.days = getDaysItem(item, itemObj)
  itemObj.freq = getFreq(item)

  itemObj.save()
  savePrices(item, itemObj.id)

def savePrices(item, itemId):
  enddate = '2999-12-31'

  if item['PRIJS2'] > 0:
    print "Newer price"
    price = float(item['PRIJS2'])/100
    begindate = item['PRIJS2DA']
    savePrice(itemId, price, begindate, enddate)

    enddate = item['PRIJS2DA']
    delta = datetime.timedelta(days=1)
    enddate = enddate - delta

  begindate = '1990-01-01'
  price = float(item['PRIJS'])/100
  savePrice(itemId, price, begindate, enddate)

def savePrice(itemId, price, begindate, enddate):
  priceObj = Price()
  priceObj.item_id = itemId
  priceObj.price = price
  priceObj.begindate = begindate
  priceObj.enddate = enddate

  priceObj.save()

def getDaysItem(item, itemObj):
  days = 0

  if item['FREKW'] == 'D':

    for i in range(2, 7):
      
      if item['LEV' + str(i)] == 'Y':
        days = days + itemObj.getDayBit(i-2)

    return days
  elif item['FREKW'] == 'W':
    return itemObj.getDayBitByDate(item['LEVOP'])

  return days

def getFreq(item):
  if item['FREKW'] == 'D':
    return 1
  elif item['FREKW'] == 'W':
    return 2
  elif item['FREKW'] == 'V':
    return 3
  elif item['FREKW'] == 'M':
    return 4
  else:
    print item

  return 0

db = dbf.Dbf("migrate/KR_DIENS.DBF")

print "Migrate items"
print "============="

Item.objects.all().delete()

for item in db:
  saveItem(item)
