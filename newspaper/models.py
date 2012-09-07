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

class Item(models.Model):
  name = models.CharField('Naam', max_length=255)
  description = models.CharField('Beschrijving', max_length=255)
  days = models.IntegerField()

  def isDeliveryDay(self, date, days):
    day = int(date.weekday()) + 1
    check = pow(2, day)

    if days & check > 0:
      return True
    else:
      return False
 
class Price(models.Model):
  begindate = models.CharField(max_length=255)
  enddate = models.CharField(max_length=255)
  item_id = models.IntegerField('Artikel')

class Holiday(models.Model):
  begindate = models.DateField()
  enddate = models.DateField()
  client_id = models.IntegerField()
 
class BankHoliday(models.Model):
  entrydate = models.DateField()

class Delivery(models.Model):
  client_id = models.IntegerField()
  item_id = models.IntegerField()
  days = models.IntegerField()
  begindate = models.DateField()
  enddate = models.DateField()
 
