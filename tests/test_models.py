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

#suite = unittest.TestLoader().loadTestsFromTestCase(TestItemModel)
#unittest.TextTestRunner(verbosity=3).run(suite)
