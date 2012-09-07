from dbfpy import dbf
import os, sys

db = dbf.Dbf("migrate/KR_KLANT.DBF")

for rec in db:
  print '=============================================================='
  print rec
  print '=============================================================='
