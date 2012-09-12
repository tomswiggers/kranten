import datetime

class Invoice:

  def __init__(self, year, month):
    self.begindate = datetime.date(year, month, 1)

    lastDayOfMonth = self.getLastDayOfMonth(self.begindate)
    self.enddate = datetime.date(year, month, lastDayOfMonth)

  def getLastDayOfMonth(self, date):
    nextMonth = (date.month % 12) + 1
    lastDay = datetime.date(date.year, nextMonth, 1) - datetime.timedelta(days = 1)

    return lastDay.day
