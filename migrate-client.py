from dbfpy import dbf
import os, sys
import datetime

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

from django.db import models
from django.core.management import call_command

from newspaper.models import Client

class Client_Tmp:
  def __str__(self):
    return str(self.ID) + ';' + self.name + ';' + self.firstname + ';' + str(self.round_nbr) + ';' + str(self.order) + ';' + str(self.saldo)

  def __repr__(self):
    return repr((self.ID, self.name, self.street, self.number, self.round_nbr, self.order))

  def __init__(self, client):
    self.ID = client['KLANT']
    self.name = client['NAAM']
    self.firstname = client['VNAAM']
    self.street = client['STRAAT']
    self.number = client['HUISNR']
    self.box = client['BUSNR']
    self.city = client['GEMEENTE']
    self.pc = client['POSTNR']
    self.round_nbr = self.getRoundNbr(client['TOER'])
    self.order = client['VOLG']

    self.delivery_begindate = self.getDate(client['LEVVAN'], 2000, 1, 1)
    self.delivery_enddate = self.getDate(client['LEVTOT'], 2999, 12, 31)

    self.prepay = self.getPrePay(client)
    self.saldo = self.getSaldo(client)

  def getPrePay(self, client):

    if client['FAKVOOR'] == 'J':

      if client['FAKSYS'] == 'M':
        return 1
      elif client['FAKSYS'] == 'K':
        return 2
      else:
        print '---------------------------Unkown faksys'
        return 3
    elif client['FAKVOOR'] == 'N':
      return 0
    else:
      print '+++++++++++++++++++++++++++++++++++++++++++Prepay problem'
  
  def getSaldo(self, client):
    saldo = float(0)

    if client['VRSTSAL'] > 0:
      saldo = float(float(client['VRSTSAL'])/100)
      print saldo
    
    return saldo

  def getRoundNbr(self, round):
    round_nbr = 0

    if round == 'A':
      round_nbr = 1
    elif round == 'B':
      round_nbr = 2
    elif round == 'C':
      round_nbr = 3

    return round_nbr

  def getDate(self, entrydate, year, month, day):
    if type(entrydate).__name__ == 'date':
      return entrydate
    else:
      return datetime.date(year, month, day)

def saveClients(clients, round_nbr):
  print '=================================================='
  print 'Clients from round ' + str(round_nbr)

  counter = 0

  for client_tmp in sorted(clients, key=lambda client: client.order):
    print client_tmp
    client = Client()

    for field in Client._meta.fields:
      print field.name

      if hasattr(client_tmp, field.name):
        print getattr(client_tmp, field.name)
        setattr(client, field.name, getattr(client_tmp, field.name))
      
      client.id = client_tmp.ID
      client.order = counter
    
    client.save()

    counter = counter + 1

Client.objects.all().delete()

db = dbf.Dbf("migrate/KR_KLANT.DBF")
clients_round1 = []
clients_round2 = []
clients_round3 = []

for client in db:
  client = Client_Tmp(client)
  print client

  if (client.round_nbr == 1):
    clients_round1.append(client)
  elif (client.round_nbr == 2):
    clients_round2.append(client)
  elif (client.round_nbr == 3):
    clients_round3.append(client)


saveClients(clients_round1, 1)
saveClients(clients_round2, 2)
saveClients(clients_round3, 3)
