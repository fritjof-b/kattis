import sys

for i in sys.stdin:
    arguments = int(i)
    for x in range(arguments):
        print(f'{x + 1} Abracadabra')
    break
