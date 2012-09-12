import os, sys

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"

import datetime
from datetime import date

import unittest

from invoice import Invoice

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
   
