rm newspaper.db
python syncdb.py
python migrate-client.py
python migrate-holidays.py
python populate-bank-holidays.py 
python migrate-items.py
python migrate-delivery.py

python insert-holidays.py
python insert-new-client.py
python update-saldos.py
python update-prices.py
