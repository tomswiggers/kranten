import datetime
import os, sys
 
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

from django.db import models
from django.core.management import call_command

from newspaper.models import *


class Invoice:

  def __init__(self, year, month):
    self.year = year
    self.month = month

    self.begindate = datetime.date(year, month, 1)
    lastDayOfMonth = self.getLastDayOfMonth(self.begindate)
    self.enddate = datetime.date(year, month, lastDayOfMonth)

  def getLastDayOfMonth(self, date):
    nextMonth = (date.month % 12) + 1
    lastDay = datetime.date(date.year, nextMonth, 1) - datetime.timedelta(days = 1)

    return lastDay.day

  def calculateInvoice(self):
    query = Client.objects
    #query = query.filter(delivery_begindate__lte=self.begindate)
    #query = query.filter(delivery_enddate__gte=self.enddate)

    clients = query.order_by('round_nbr', 'order').all()
    
    for client in clients:
      deliveries = self.getDeliveries(client)

      if deliveries:
        print client

  def getDeliveries(self, client):
    flag = False
    currentDate = self.begindate

    deliveries = self.getDeliveriesForMonth(client.id)

    print deliveries
    for delivery in deliveries:
      print delivery


    while currentDate <= self.enddate:

      if client.isDeliveryDay(client, currentDate):
        flag = True

      currentDate = currentDate + datetime.timedelta(days = 1)

    if flag:
      return True
    else:
      return False

  def getDeliveriesForMonth(self, clientId):
    query = Delivery.objects
    #query = query.filter(begindate__year__lte=self.year)
    #query = query.filter(enddate__year__gte = self.year)
    #query = query.filter(begindate__month__lte = self.month)
    #query = query.filter(enddate__month__gte = self.month)
    query = query.filter(client_id=clientId)

    return query.all()

    
