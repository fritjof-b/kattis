#!/usr/local/bin/python3
n = int(input())
teams = {}
for _ in range(n):
    uni, team = input().split()
    if uni not in teams.keys():
        teams[uni] = [team]
    else:
        teams[uni].append(team)

for key in [team for team in list(teams.keys())[:12]]:
    print(key, teams[key][0])