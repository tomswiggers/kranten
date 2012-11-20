from django.db import models

import datetime
from datetime import date

class BankHoliday(models.Model):
  entrydate = models.DateField()

  class Meta:
    app_label = "newspaper"


