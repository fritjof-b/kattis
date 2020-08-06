#!/usr/bin/python3
number_of_tasks, max_time = list(map(int, input().split()))
tasks = list(map(int, input().split()))

used_time = 0
completed_tasks = 0

for task in tasks:
    if not used_time + task > max_time:
        used_time += task
        completed_tasks += 1
    else:
        break

print(completed_tasks)