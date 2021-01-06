#!/Users/fritjof/anaconda3/bin/python3
# problem: wertyu, rating: 3.1
import sys

correction = {
    'B' : 'V',
    'C' : 'X',
    'D' : 'S',
    'E' : 'W',
    'F' : 'D',
    'G' : 'F',
    'H' : 'G',
    'I' : 'U',
    'J' : 'H',
    'K' : 'J',
    'L' : 'K',
    'M' : 'N',
    'N' : 'B',
    'O' : 'I',
    'P' : 'O',
    'R' : 'E',
    'S' : 'A',
    'T' : 'R',
    'U' : 'Y',
    'V' : 'C',
    'W' : 'Q',
    'X' : 'Z',
    'Y' : 'T',
    '[' : 'P',
    ';' : 'L',
    ']' : '[',
    '\'': ';',
    '/' : '.',
    '.' : ',',
    ',' : 'M',
    ' ' : ' ',
    'Z' : '`',
    '1' : '`',
    '2' : '1',
    '3' : '2',
    '4' : '3',
    '5' : '4',
    '6' : '5',
    '7' : '6',
    '8' : '7',
    '9' : '8',
    '0' : '9',
    '-' : '0',
    '=' : '-',
    '\\' : ']'
}

to_correct = sys.stdin.read().strip('\n')
s = []
for c in to_correct:
    if c != '\n':
        s.append(correction[c])
    elif c == '\n':
        s.append(' ')

print("".join(s))
