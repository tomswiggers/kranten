import os, sys

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
 
from django.core.management import call_command
 
from newspaper.models import Client
from django.db import models

import datetime
from datetime import date

import unittest

class TestClientModel(unittest.TestCase):

  def setUp(self):
    self.client = Client()
    self.client.delivery_begindate = date(2012, 9, 3)
    self.client.delivery_enddate = date(2012, 9, 6)

  def test_dayBefore(self):
    self.assertEqual(False, self.client.isDeliveryDay(self.client, date(2012, 9, 2)))

  def test_dayAfter(self):
    self.assertEqual(False, self.client.isDeliveryDay(self.client, date(2012, 9, 7)))  
  
  def test_dayBegindate(self):
    self.assertEqual(True, self.client.isDeliveryDay(self.client, date(2012, 9, 3)))
  
  def test_dayEnddate(self):
    self.assertEqual(True, self.client.isDeliveryDay(self.client, date(2012, 9, 6)))

  def test_dayInMiddle(self):
    self.assertEqual(True, self.client.isDeliveryDay(self.client, date(2012, 9, 5)))
