import os, sys

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

import datetime
from datetime import date

import unittest

from invoice import Invoice

from newspaper.models import *
from django.db import models

class TestInvoice(unittest.TestCase):

  def setUp(self):
    self.invoice = Invoice(2012, 1)

  def test_getLastDayOfMonth(self):
    self.assertEqual(31, self.invoice.getLastDayOfMonth(date(2012, 1, 1)))
    self.assertEqual(29, self.invoice.getLastDayOfMonth(date(2012, 2, 1)))
    self.assertEqual(31, self.invoice.getLastDayOfMonth(date(2012, 3, 1)))
    self.assertEqual(30, self.invoice.getLastDayOfMonth(date(2012, 4, 1)))
    self.assertEqual(31, self.invoice.getLastDayOfMonth(date(2012, 5, 1)))
    self.assertEqual(31, self.invoice.getLastDayOfMonth(date(2012, 12, 1)))

  def test_getBeginDatePreviousMonth(self):
    self.assertEqual(date(2011, 12, 1), self.invoice.getBeginDatePreviousMonth(date(2012, 1, 25)))
    self.assertEqual(date(2012, 1, 1), self.invoice.getBeginDatePreviousMonth(date(2012, 2, 25)))
    self.assertEqual(date(2012, 11, 1), self.invoice.getBeginDatePreviousMonth(date(2012, 12, 25)))
  
  def test_getBeginDateNextMonth(self):
    self.assertEqual(date(2012, 1, 1), self.invoice.getBeginDateNextMonth(date(2011, 12, 3)))
    self.assertEqual(date(2012, 2, 1), self.invoice.getBeginDateNextMonth(date(2012, 1, 3)))
    self.assertEqual(date(2012, 3, 1), self.invoice.getBeginDateNextMonth(date(2012, 2, 3)))
    self.assertEqual(date(2012, 4, 1), self.invoice.getBeginDateNextMonth(date(2012, 3, 3)))
    self.assertEqual(date(2012, 5, 1), self.invoice.getBeginDateNextMonth(date(2012, 4, 3)))
    self.assertEqual(date(2012, 6, 1), self.invoice.getBeginDateNextMonth(date(2012, 5, 3)))
    self.assertEqual(date(2012, 7, 1), self.invoice.getBeginDateNextMonth(date(2012, 6, 3)))
    self.assertEqual(date(2012, 8, 1), self.invoice.getBeginDateNextMonth(date(2012, 7, 3)))
    self.assertEqual(date(2012, 9, 1), self.invoice.getBeginDateNextMonth(date(2012, 8, 3)))
    self.assertEqual(date(2012, 10, 1), self.invoice.getBeginDateNextMonth(date(2012, 9, 3)))
    self.assertEqual(date(2012, 11, 1), self.invoice.getBeginDateNextMonth(date(2012, 10, 3)))
    self.assertEqual(date(2012, 12, 1), self.invoice.getBeginDateNextMonth(date(2012, 11, 3)))

  def test_getEndDateQuarter(self):
    self.assertEqual(date(2012, 3, 31), self.invoice.getEndDateQuarter(date(2011, 12, 31)))
    self.assertEqual(date(2012, 6, 30), self.invoice.getEndDateQuarter(date(2012, 3, 31)))
    self.assertEqual(date(2012, 9, 30), self.invoice.getEndDateQuarter(date(2012, 6, 30)))
    self.assertEqual(date(2012, 12, 31), self.invoice.getEndDateQuarter(date(2012, 9, 3)))

  def test_isDeliveryForMonth(self):
    delivery = Delivery()

    delivery.begindate = date(2012, 1, 10)
    delivery.enddate = date(2012, 1, 20)

    self.assertFalse(self.invoice.isDeliveryForMonth(delivery, date(2011, 12, 1), date(2011, 12, 31)));
    self.assertTrue(self.invoice.isDeliveryForMonth(delivery, date(2012, 1, 1), date(2012, 1, 31)));
    self.assertFalse(self.invoice.isDeliveryForMonth(delivery, date(2012, 2, 1), date(2012, 2, 28)));

  def test_isHoliday(self):
    holidays = list()
    
    holiday = Holiday()

    holiday.begindate = date(2012, 1, 20)
    holiday.enddate = date(2012, 2, 4)

    holidays.append(holiday)

    holiday2 = Holiday()
    holiday2.begindate = date(2012, 3, 2)
    holiday2.enddate = date(2012, 3, 4)

    holidays.append(holiday2)

    self.assertFalse(self.invoice.isHoliday(holidays, date(2012, 1, 19)))
    self.assertTrue(self.invoice.isHoliday(holidays, date(2012, 1, 20)))
    self.assertTrue(self.invoice.isHoliday(holidays, date(2012, 1, 22)))
    self.assertTrue(self.invoice.isHoliday(holidays, date(2012, 2, 3)))
    self.assertTrue(self.invoice.isHoliday(holidays, date(2012, 2, 4)))
    self.assertFalse(self.invoice.isHoliday(holidays, date(2012, 2, 5)))
    self.assertFalse(self.invoice.isHoliday(holidays, date(2012, 3, 1)))
    self.assertTrue(self.invoice.isHoliday(holidays, date(2012, 3, 2)))
    self.assertTrue(self.invoice.isHoliday(holidays, date(2012, 3, 4)))
    self.assertFalse(self.invoice.isHoliday(holidays, date(2012, 3, 5)))

  def test_getWeekNumber(self):
    self.assertEqual(1, self.invoice.getWeekNumber(date(2012, 9, 1)))
    self.assertEqual(1, self.invoice.getWeekNumber(date(2012, 9, 2)))
    self.assertEqual(1, self.invoice.getWeekNumber(date(2012, 9, 3)))
    self.assertEqual(1, self.invoice.getWeekNumber(date(2012, 9, 9)))
    self.assertEqual(2, self.invoice.getWeekNumber(date(2012, 9, 10)))
    self.assertEqual(2, self.invoice.getWeekNumber(date(2012, 9, 16)))
    self.assertEqual(3, self.invoice.getWeekNumber(date(2012, 9, 17)))
    self.assertEqual(3, self.invoice.getWeekNumber(date(2012, 9, 23)))
    self.assertEqual(4, self.invoice.getWeekNumber(date(2012, 9, 24)))
