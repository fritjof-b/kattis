import re

read_nbr = int(input())
text = []
days = 0
msg = 'I must watch Star Wars with my daughter'

for i in range(read_nbr):
    text.append(input())

for line in text:
    if re.search(r'rose', line, flags = re.I) or re.search(r'pink', line, flags = re.I):
        days += 1

if days > 0:
    msg = days

print(msg)
