from django.db import models

import datetime
from datetime import date

class Price(models.Model):
  begindate = models.DateField()
  enddate = models.DateField()
  price = models.FloatField('Prijs')
  item_id = models.IntegerField('Artikel')

  def __str__(self):
    return str(self.id) + ';' + str(self.price) + ';' + str(self.item_id)

