import os

class Config:
  width = 600
  height = 600
  dbEngine = "django.db.backends.sqlite3"
  dbName = "newspaper.db"
  dirBase = os.path.dirname(os.path.abspath(__file__))
  dbFilename = dirBase + "/" + dbName
  dirBackup = dirBase + "/backup"


