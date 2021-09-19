import datetime
from dateutil import parser
import pytz

print("date: ", datetime.date(year=2001, month=1, day=12))
print("today(): ", datetime.date.today())
print("time: ", datetime.time(hour=5, minute=20), '\n')

now = datetime.datetime.now()
print("utcnow(): ", datetime.datetime.utcnow())
print("timedelta: ", now + datetime.timedelta(days=365))
print("weekday: ", datetime.datetime.weekday(now), '\n')

print("isoformat(): ", datetime.datetime.isoformat(now))
print("strftime(): ", now.strftime('%d/%m/%y'))
print("strptime(): ", datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M"))
print("parse(): ", parser.parse("4th of July, 2015"), '\n')

print(pytz.timezone('UTC'))
