#! /usr/bin/python3

import sys

def main():
    x = int(input())
    y = int(input())
    if x > 0:
        if y > 0:
            retval = 1
        elif y < 0:
            retval = 4
    elif x < 0:
        if y > 0:
            retval = 2
        elif y < 0:
            retval = 3
        
    print(retval)

if __name__ == "__main__":
    main()
