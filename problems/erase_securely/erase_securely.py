import sys

overwrite_times = int(input())
first_string = input()
second_string = input()

checked_strings = []

for i in range(overwrite_times):
    check_string = []
    for j in (first_string):
        if j == '0':
            check_string.append('1')
        elif j == '1':
            check_string.append('0')
    
    first_string = "".join(check_string)

if first_string == second_string:
    print('Deletion succeeded')
else:
    print('Deletion failed')
