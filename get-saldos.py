import sys

from invoice import Invoice

year = int(sys.argv[1])
month = int(sys.argv[2])

invoice = Invoice(year, month)
invoice.calculateSaldos()
