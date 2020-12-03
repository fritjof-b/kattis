#!/Users/fritjof/anaconda3/bin/python3
# problem: datum, rating: 1.4
import datetime

d, m = [int(_) for _ in input().split()]

d = datetime.date(2009, m, d).weekday()
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

print(weekdays[d])
