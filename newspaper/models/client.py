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

  class Meta:
    app_label = "newspaper"

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

