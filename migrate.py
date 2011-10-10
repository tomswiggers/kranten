from dbfpy import dbf
import os, sys
 
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

from django.db import models
from django.core.management import call_command

from newspaper.models import Client

db = dbf.Dbf("migrate/KR_KLANT.DBF")

for rec in db:
  print rec
  
  client = Client()
  client.ID = rec['KLANT']
  client.name = rec['NAAM']
  client.firstname = rec['VNAAM']
  client.street = rec['STRAAT']
  client.number = rec['HUISNR']
  client.box = rec['BUSNR']

  if rec['TOER'] == 'A':
    round = 1
  elif rec['TOER'] == 'B':
    round = 2
  elif rec['TOER'] == 'C':
    round = 3

  client.round = round
  client.order = int(rec['VOLG'])

  client.save()
