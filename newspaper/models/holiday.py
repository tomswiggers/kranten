from django.db import models

import datetime
from datetime import date

class Holiday(models.Model):
  begindate = models.DateField()
  enddate = models.DateField()
  client_id = models.IntegerField()

  def __str__(self):
    return str(self.client_id) + ';' + str(self.begindate) + ';' + str(self.enddate)

