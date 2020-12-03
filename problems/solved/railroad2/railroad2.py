#!/Users/fritjof/anaconda3/bin/python3
from os import read
y = int(read(0,20).split()[1])
if y % 2 == 0: 
    print('possible')
else:
    print('impossible')
