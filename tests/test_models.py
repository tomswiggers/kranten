import os, sys

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
 
from django.core.management import call_command
 
from newspaper.models import Item
from django.db import models

import datetime
from datetime import date

import unittest

class TestItemModel(unittest.TestCase):

  def setUp(self):
    self.item = Item()

  def test_isDeliveryDay(self):
    self.assertEqual(True, self.item.isDeliveryDay(date(2012, 9, 3), 2), 'Test Monday')
    self.assertEqual(True, self.item.isDeliveryDay(date(2012, 9, 4), 4))
    self.assertEqual(True, self.item.isDeliveryDay(date(2012, 9, 5), 8))
    self.assertEqual(True, self.item.isDeliveryDay(date(2012, 9, 6), 16))
    self.assertEqual(True, self.item.isDeliveryDay(date(2012, 9, 7), 32))
    self.assertEqual(True, self.item.isDeliveryDay(date(2012, 9, 8), 64))
    
    self.assertEqual(True, self.item.isDeliveryDay(date(2012, 9, 3), 6))
    self.assertEqual(True, self.item.isDeliveryDay(date(2012, 9, 3), 10))
    self.assertEqual(True, self.item.isDeliveryDay(date(2012, 9, 3), 18))

    self.assertEqual(True, self.item.isDeliveryDay(date(2012, 9, 3), 62), 'Test Monday')
    self.assertEqual(True, self.item.isDeliveryDay(date(2012, 9, 4), 62))
    self.assertEqual(True, self.item.isDeliveryDay(date(2012, 9, 5), 62))
    self.assertEqual(True, self.item.isDeliveryDay(date(2012, 9, 6), 62))
    self.assertEqual(True, self.item.isDeliveryDay(date(2012, 9, 7), 62))

  def test_getDay(self):
    self.assertEqual(2, self.item.getDayBitByDate(date(2012, 9, 3)), 'Test Monday')
    self.assertEqual(4, self.item.getDayBitByDate(date(2012, 9, 4)), 'Test Tuesday')
    self.assertEqual(8, self.item.getDayBitByDate(date(2012, 9, 5)), 'Test Wednesday')
    self.assertEqual(16, self.item.getDayBitByDate(date(2012, 9, 6)), 'Test Thursday')
    self.assertEqual(32, self.item.getDayBitByDate(date(2012, 9, 7)), 'Test Friday')
    self.assertEqual(64, self.item.getDayBitByDate(date(2012, 9, 8)), 'Test Saturday')

  def test_getDayBit(self):
    self.assertEqual(2, self.item.getDayBit(0))
    self.assertEqual(4, self.item.getDayBit(1))
    self.assertEqual(8, self.item.getDayBit(2))
    self.assertEqual(16, self.item.getDayBit(3))
    self.assertEqual(32, self.item.getDayBit(4))
    self.assertEqual(64, self.item.getDayBit(5))
