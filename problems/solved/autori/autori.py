import sys

for i in sys.stdin:
    args = i.split('-')
    output = ""
    for string in args:
        output += string[0]
    print(output)
