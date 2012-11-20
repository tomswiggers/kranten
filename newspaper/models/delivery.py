from django.db import models

import datetime
from datetime import date

class Delivery(models.Model):
  client_id = models.IntegerField()
  item_id = models.IntegerField()
  days = models.IntegerField()
  begindate = models.DateField()
  enddate = models.DateField()
  
  class Meta:
    app_label = "newspaper"

  def __str__(self):
    return 'Delivery Object(client_id, item_id, days, begindate, enddate): ' + str(self.client_id) + ', ' + str(self.item_id) + ', ' + str(self.days) + ', ' + str(self.begindate) + ', ' + str(self.enddate)


