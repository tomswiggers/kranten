from django.db import models

class MyModel(models.Model):
  field = models.CharField(max_length=255)
  
  def __unicode__(self):
    return self.field

class Client(models.Model):
  name = models.CharField('Naam', max_length=255)
  firstname = models.CharField('Voornaam', max_length=255)
  street = models.CharField('Straat', max_length=255)
  number = models.CharField('Nummer', max_length=255)
  box = models.CharField('Bus', max_length=255)
  pc = models.CharField('Postcode', max_length=255)
  city = models.CharField('Gemeente', max_length=255)
  order = models.CharField('Volgorde in ronde', max_length=255)

class Holiday(models.Model):
  begindate = models.CharField(max_length=255)
  enddate = models.CharField(max_length=255)
  client = models.CharField(max_length=255)
