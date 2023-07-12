from datetime import datetime


now = datetime.now()
print('date time now: ', now)

print('year: ', now.year)
print('month: ', now.month)
print('day: ', now.day)
print('hour: ', now.hour)
print('minute: ', now.minute)
print('second: ', now.second)

print('now in another format: ', datetime.ctime(now))
print('now in another formats: ', datetime.strftime(now, '%Y'))
print('now in another formats: ', datetime.strftime(now, '%B'))
print('now in another formats: ', datetime.strftime(now, '%A'))
print('now in another formats: ', datetime.strftime(now, '%X'))
print('now in another formats: ', datetime.strftime(now, '%d'))

t = '13 April 2018 hour 12:40:59'
dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
print(dt)

birthday = datetime(2008, 8, 16, 12, 13, 59)
tstamp = datetime.timestamp(birthday)
print(tstamp)

birth_from_tstamp = datetime.fromtimestamp(tstamp)
print(birth_from_tstamp)