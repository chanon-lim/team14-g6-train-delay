from datetime import datetime, timedelta

now = datetime.now()
now_str = now.strftime('%Y-%m-%d %H:%M')
print(now_str)

now2 = datetime.strptime(now_str, '%Y-%m-%d %H:%M')
print(now2)
print(type(now2))

time1 = datetime(2021, 12, 22, 12, 6)
time2 = datetime(2021, 12, 22, 12, 12)
print(time2-time1)
# 0:06:00
print((time2-time1) > timedelta(minutes=5))
# True