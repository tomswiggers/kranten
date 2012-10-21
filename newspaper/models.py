from django.db import models

import datetime
from datetime import date

class Client(models.Model):
  name = models.CharField('Naam', max_length=255)
  firstname = models.CharField('Voornaam', max_length=255)
  street = models.CharField('Straat', max_length=255)
  number = models.CharField('Nummer', max_length=255)
  box = models.CharField('Bus', max_length=255)
  pc = models.CharField('Postcode', max_length=255)
  city = models.CharField('Gemeente', max_length=255)
  round_nbr = models.IntegerField('Ronde')
  order = models.IntegerField('Volgorde in ronde')
  delivery_begindate = models.DateField()
  delivery_enddate = models.DateField()
  prepay = models.IntegerField()
  freq = models.IntegerField()
  saldo = models.FloatField()

  def isActive(self, client, entrydate):

    if client.delivery_begindate <= entrydate and client.delivery_enddate >= entrydate:
      return True
    else:
      return False
  
  def __repr__(self):
    return self.getString()

  def __str__(self):
    return self.getString()

  def getString(self):
    return str(self.id) + ';' + self.name + ';' + self.firstname + ';' + str(self.round_nbr) + ';' + str(self.order) + ';' + str(self.saldo)

class Item(models.Model):
  name = models.CharField('Naam', max_length=255)
  description = models.CharField('Beschrijving', max_length=255)
  days = models.IntegerField()
  freq = models.IntegerField()

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

class Price(models.Model):
  begindate = models.DateField()
  enddate = models.DateField()
  price = models.FloatField('Prijs')
  item_id = models.IntegerField('Artikel')

  def __str__(self):
    return str(self.id) + ';' + str(self.price) + ';' + str(self.item_id)

class Holiday(models.Model):
  begindate = models.DateField()
  enddate = models.DateField()
  client_id = models.IntegerField()

  def __str__(self):
    return str(self.client_id) + ';' + str(self.begindate) + ';' + str(self.enddate)

class BankHoliday(models.Model):
  entrydate = models.DateField()

class Delivery(models.Model):
  client_id = models.IntegerField()
  item_id = models.IntegerField()
  days = models.IntegerField()
  begindate = models.DateField()
  enddate = models.DateField()
  
  def __str__(self):
    return 'Delivery Object(client_id, item_id, days, begindate, enddate): ' + str(self.client_id) + ', ' + str(self.item_id) + ', ' + str(self.days) + ', ' + str(self.begindate) + ', ' + str(self.enddate)


