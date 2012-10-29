from django.db import models

import datetime
from datetime import date

class Item(models.Model):
  name = models.CharField('Naam', max_length=255)
  description = models.CharField('Beschrijving', max_length=255)
  days = models.IntegerField()
  freq = models.IntegerField()

  class Meta:
    app_label = "newspaper"

  def __str__(self):
    return str(self.id) + ';' + self.name + ', ' + str(self.days) + ', ' + str(self.freq)

  def isDeliveryDay(self, date, days):
    check = self.getDayBitByDate(date)

    if days & check > 0:
      return True
    else:
      return False
  
  def getDayBit(self, weekday):
    return pow(2, int(weekday) + 1)

  def getDayBitByDate(self, date):
    day = int(date.weekday()) + 1
    return pow(2, day)

  def getItemByName(self, name):
    return Item.objects.get(name = name)
 
  #@todo build in proper checks
  def getItemIdByName(self, name):
    item = self.getItemByName(name)
    return item.id

