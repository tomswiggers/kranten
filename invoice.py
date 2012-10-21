import datetime
import time
import os, sys
 
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

from django.db import models
from django.core.management import call_command
from django.db import connection

from newspaper.models import *

from configmerchant import ConfigMerchant

class Invoice:

  MONTH = 1
  BIMONTH = 2
  QUARTER = 3
  BIYEAR = 4
  YEAR = 5


  def __init__(self, year, month):
    self.year = year
    self.month = month

    self.beginDate = datetime.date(year, month, 1)
    self.endDate = self.getEndDateMonth(self.beginDate)

  def log(self, msg):
    timestamp = datetime.datetime.now()
    print timestamp.isoformat() + ': ' + str(msg)

  def getLastDayOfMonth(self, date):
    nextMonth = (date.month % 12) + 1
    lastDay = datetime.date(date.year, nextMonth, 1) - datetime.timedelta(days = 1)

    return lastDay.day

  def getEndDateMonth(self, entryDate):
    return datetime.date(entryDate.year, entryDate.month, self.getLastDayOfMonth(entryDate))

  def getEndDateNextMonth(self, entryDate):
    beginDateNextMonth = self.getBeginDateNextMonth(entryDate)
    return datetime.date(beginDateNextMonth.year, beginDateNextMonth.month, self.getLastDayOfMonth(beginDateNextMonth))

  def getBeginDatePreviousMonth(self, entryDate):
    month = entryDate.month - 1

    if month == 0:
      month = 12
      year = entryDate.year - 1
    else:
      year = entryDate.year

    return date(year, month, 1)

  def getBeginDateNextMonth(self, entryDate):
    month = (entryDate.month % 12) + 1

    if month == 1:
      year = entryDate.year + 1
    else:
      year = entryDate.year

    return date(year, month, 1)

  def getEndDateQuarter(self, entryDate):

    for i in [1,2,3]:
      entryDate = self.getEndDateNextMonth(entryDate)

    return entryDate

  def getClients(self):
    return Client.objects.order_by('round_nbr', 'order').all()

  def getClientsWithSaldo(self):
    return Client.objects.filter(saldo__gt=0).all()

  def calculateInvoice(self):
    invoices = self.getInvoiceList(self.getClients())

    self.writeList(invoices)
    self.writeInvoices(invoices)

  def calculateSaldos(self):
    clients = self.getClientsWithSaldo()
    invoices = self.getInvoiceList(clients)
    print invoices

    self.printSaldos(invoices)

  def getInvoiceList(self, clients):
    self.log('Start')
    invoices = list()
       
    for client in clients:
      flag = True
      self.log('Start getInvoice: ' + str(client))

      beginDate = self.beginDate
      endDate = self.endDate

      if client.prepay == 1:

        if client.freq == self.MONTH:
          print "===== PREPAY MONTH ====="
          beginDate = self.getBeginDateNextMonth(beginDate)
          endDate = self.getEndDateMonth(beginDate)
        elif client.freq == self.QUARTER and beginDate.month % 3 == 0:
          print "===== PREPAY QUARTER ====="
          beginDate = self.getBeginDateNextMonth(beginDate)
          endDate = self.getEndDateQuarter(endDate)
        else:
          print "===== PREPAY NOK ====="
          flag = False
      else:

        if client.freq == self.BIMONTH and beginDate.month % 2 == 0:
          print "===== BIMONTH ====="

          beginDate = self.getBeginDatePreviousMonth(beginDate)
          print beginDate
          print endDate

      if flag:
        invoices.append(self.getInvoice(client, beginDate, endDate))

      self.log('End getInvoice: ' + str(client))

    return invoices

  def getInvoice(self, client, beginDate, endDate):
    flag = True
    invoices = dict()

    currentDate = beginDate

    deliveries = self.getDeliveries(client.id)
    holidays = self.getHolidays(client.id)

    while currentDate <= endDate:

      #check if client has a holiday
      if self.isHoliday(holidays, currentDate):
        flag = False

      #check if client is active
      if not client.isActive(client, currentDate):
        flag = False

      if flag:
        invoicesPerDay = self.processDeliveries(client, deliveries, currentDate)
        
        for invoicePerDay in invoicesPerDay:

          #check client already in invoice list
          if not invoices.has_key(client.id):
            invoices[client.id] = {'client': client, 'deliveries': {}, 'beginDate': beginDate, 'endDate': endDate}

          #check if price is already in delivery list for client
          if not invoices[client.id]['deliveries'].has_key(invoicePerDay['price'].id):
            invoices[client.id]['deliveries'][invoicePerDay['price'].id] = {'total': 1, 'price': invoicePerDay['price'], 'item': invoicePerDay['item']}
          else:
            flagMonthly = False
            flagBiWeekly = False

            #Add monthly items only once per month
            if self.isMonthlyItemAlreadyInList(invoices[client.id]['deliveries'][invoicePerDay['price'].id]):
              flagMonthly = True

            #Add bi-weekly items only once per week
            if self.isWeeklyItemAlreadyInList(invoices[client.id]['deliveries'][invoicePerDay['price'].id], currentDate):
              flagBiWeekly = True

            if not flagMonthly and not flagBiWeekly:
              invoices[client.id]['deliveries'][invoicePerDay['price'].id]['total'] = invoices[client.id]['deliveries'][invoicePerDay['price'].id]['total'] + 1
              invoices[client.id]['deliveries'][invoicePerDay['price'].id]['item'].weekNumber = self.getWeekNumber(currentDate)

      flag = True
      currentDate = currentDate + datetime.timedelta(days = 1)

    return invoices
 
  def isMonthlyItemAlreadyInList(self, delivery):

    if delivery['item'].freq == 4:
      return True
    else:
      return False

  def isWeeklyItemAlreadyInList(self, delivery, currentDate):
    
    if delivery['item'].freq == 3:
      weekNumber = self.getWeekNumber(currentDate)

      if weekNumber == delivery['item'].weekNumber:
        return True
      else:
        print "add item"
        return False
    else:
      return False

  def getDeliveries(self, clientId):
    deliveries = list()

    query = Delivery.objects
    query = query.filter(client_id=clientId)

    return query.all()

  def isDeliveryForMonth(self, delivery, begindate, enddate):
    delta = datetime.timedelta(days=1)
    entrydate = begindate

    while entrydate <= enddate:
      
      if entrydate >= delivery.begindate and entrydate <= delivery.enddate:
        return True
      else:
        entrydate = entrydate + delta

    return False

  def getHolidays(self, clientId):
    return Holiday.objects.filter(client_id = clientId).all()

  def isHoliday(self, holidays, currentDate):

    for holiday in holidays:

      if holiday.begindate <= currentDate and holiday.enddate >= currentDate:
        return True

    return False  

  def processDeliveries(self, client, deliveries, currentDate):
    invoices = list()

    for delivery in deliveries:

      if currentDate >= delivery.begindate and currentDate <= delivery.enddate:
        
        if (delivery.days > 0):

          if Item().isDeliveryDay(currentDate, delivery.days):
            item = self.getItem(delivery.item_id)
            price = self.getPrice(delivery.item_id, currentDate)
            invoices.append({'price': price, 'item': item, 'currentDate': currentDate})
        else:
          item = self.getItem(delivery.item_id)

          if item.freq == 2:

            if Item().isDeliveryDay(currentDate, item.days):
              price = self.getPrice(delivery.item_id, currentDate)
              invoices.append({'price': price, 'item': item, 'currentDate': currentDate})
          elif item.freq == 3:

            if self.getWeekNumber(currentDate) % 2 == 0:
              price = self.getPrice(delivery.item_id, currentDate)
              item.weekNumber = self.getWeekNumber(currentDate)
              invoices.append({'price': price, 'item': item, 'currentDate': currentDate})
          elif item.freq == 4:
            price = self.getPrice(delivery.item_id, currentDate)
            invoices.append({'price': price, 'item': item, 'currentDate': currentDate})
          else:
            print '------------------------Other freq-----------------------------'

    return invoices

  def getItem(self, itemId):
    return Item.objects.filter(id = itemId).get()
  
  def getPrice(self, itemId, currentDate):
    query = Price.objects
    query = query.filter(item_id=itemId, begindate__lte=currentDate, enddate__gte=currentDate)

    return query.get()

  def printSaldos(self, invoices):
    line = "{:<5}{:<30}{:>15}{:>25}{:>25}{:>15}"
  
    print line.format("Id", "Naam", "Vorig saldo", "Bedrag " + str(self.beginDate.strftime('%B')), "Te betalen " + str(self.beginDate.strftime('%B')), "Nieuw saldo")

    for invoice in invoices:

      if len(invoice.values()) > 0:
        total = self.getTotal(invoice.values()[0])
        client = invoice.values()[0]['client']

        pay = float(0)
        saldoNew = float(0)

        if client.saldo > total:
          pay = 0
          saldoNew = client.saldo - total
        else:
          pay = total - client.saldo
          saldoNew = 0

        print line.format(client.id, client.name, client.saldo, total, pay, saldoNew)

  def writeList(self, invoices):
    print '------------------writeList--------------------'
    filename = 'betalingslijst-' + str(self.beginDate.strftime('%B')) + '.csv'
    fp = open(filename, 'w')

    fp.write('Postcode;Gemeente;Straat;Nummer;Naam;Voornaam;Totaal;Saldo;Te betalen\n')

    #sorted(invoices, key=lambda invoice: invoice[0].street)

    for invoice in invoices:

      if len(invoice.values()) > 0:
        print invoice.values()[0]['client']
        fp.write(self.getClientSummary(invoice.values()[0]))
      else:
        print 'empty'

  def writeInvoices(self, invoices):
    filename = 'facturen-' + str(self.beginDate.strftime('%B')) + '.txt'
    fp = open(filename, 'w')

    for invoice in invoices:

      if len(invoice.values()) > 0:
        fp.write(self.getClientInvoice(invoice.values()[0]))

  def getTotal(self, invoice):
    total = float(0)

    for priceId in invoice['deliveries']:
      total = total + (invoice['deliveries'][priceId]['price'].price * invoice['deliveries'][priceId]['total'])
    
    return total

  def getClientSummary(self, invoice):
    total = self.getTotal(invoice)

    client = invoice['client']
    line = '{};{};{};{};{};{};{}\n'
    
    if total > client.saldo:
      total = total - client.saldo

    return line.format(client.pc, client.city, client.street, client.number, client.name, client.firstname, total)

  def getClientInvoice(self, invoice):
    client = invoice['client']
    deliveries = invoice['deliveries']
  
    if not client.box == "0":
      houseNumber = client.number + '/' + client.box
    else:
      houseNumber = client.number

    invoiceStr = '\r\n'
    invoiceStr = invoiceStr + '\r\n'
    invoiceStr = invoiceStr + ConfigMerchant.line1 + '\r\n'
    invoiceStr = invoiceStr + ConfigMerchant.line2 + '\r\n'
    invoiceStr = invoiceStr + ConfigMerchant.line3 + '\r\n'
    invoiceStr = invoiceStr + ConfigMerchant.line4 + date.today().isoformat() + '\r\n'
    invoiceStr = invoiceStr + '__________________________________________________________________________\r\n'
    invoiceStr = invoiceStr + 'REKENING van ' + invoice['beginDate'].isoformat() + ' tot ' + invoice['endDate'].isoformat() + '             ' + client.name + ' ' + client.firstname + '\r\n'
    invoiceStr = invoiceStr + '                                                   ' + client.street + ' ' + houseNumber + '\r\n'
    invoiceStr = invoiceStr + '                                                   ' + client.pc + ' ' + client.city + '\r\n'

    invoiceStr = invoiceStr + '\r\n'
    invoiceStr = invoiceStr + 'omschrijving                aantal               prijs              totaal\r\n'
    invoiceStr = invoiceStr + '__________________________________________________________________________\r\n'

    total = float(0)
    counter = 0

    for priceId in deliveries:
      counter = counter + 1
      totalItem = float(deliveries[priceId]['total']) * float(deliveries[priceId]['price'].price)
      total = total + totalItem
      invoiceStr = invoiceStr + "%-28s%-21s%-20s%5s\r\n" % (deliveries[priceId]['item'].description, str(deliveries[priceId]['total']), str(float(deliveries[priceId]['price'].price)), str(totalItem))

    while counter < 6:
      invoiceStr = invoiceStr + '\r\n'
      counter = counter + 1

    invoiceStr = invoiceStr + '__________________________________________________________________________\r\n'
    invoiceStr = invoiceStr + 'TOTALEN:                                                         %.2f EUR\r\n' % (total)
    invoiceStr = invoiceStr + '\r\n'

    #check prepay and saldo
    if client.saldo > 0:

      if client.saldo - total < 0:
        remaining = total - client.saldo
      else:
        remaining = float(0)

      invoiceStr = invoiceStr + 'VOORSCHOT:                                                     %.2f EUR\r\n' % (total)
      invoiceStr = invoiceStr + 'SALDO:                                                         %.2f EUR\r\n' % (client.saldo - total)
      invoiceStr = invoiceStr + 'TE BETALEN:                                                    %.2f EUR\r\n' % (remaining)

    invoiceStr = invoiceStr + '\r\n'
    invoiceStr = invoiceStr + 'Maandagnamiddag en zaterdagnamiddag gesloten  !!!\r\n'
    invoiceStr = invoiceStr + 'Gelieve de rekening in de winkel te betalen.\r\n'
    invoiceStr = invoiceStr + '\r\n'
    invoiceStr = invoiceStr + '\r\n'
    invoiceStr = invoiceStr + '\r\n'

    if client.saldo == 0:
      invoiceStr = invoiceStr + '\r\n'
      invoiceStr = invoiceStr + '\r\n'
      invoiceStr = invoiceStr + '\r\n'

    invoiceStr = invoiceStr + '\r\n'
    invoiceStr = invoiceStr + '\r\n'
    invoiceStr = invoiceStr + '\r\n'

    return invoiceStr

  def getWeekNumber(self, entryDate):
    currentDate = date(entryDate.year, entryDate.month, 1)
    delta = datetime.timedelta(days=1)
    counter = 1

    while currentDate <= entryDate:

      if (currentDate.weekday()+1) % 7 == 1 and currentDate.day > 3:
        counter = counter + 1
        
      currentDate = currentDate + delta

    return counter
