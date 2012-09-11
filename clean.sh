rm newspaper.db
python syncdb.py
python migrate-client.py
python migrate-holidays.py
python populate-bank-holidays.py 
python migrate-items.py
