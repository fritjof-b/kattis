#!/Users/fritjof/anaconda3/bin/python3
# problem: mia, rating: 2.0

while True:
    d = input()
    if d == '0 0 0 0': break
    d = d.split()
    p1 = "".join(sorted(d[:2]))
    p2 = "".join(sorted(d[2:]))

    if p1 == p2:
        print('Tie.')
    elif p1 == '12' and p2 != '12':
        print('Player 1 wins.')
    elif p1 != '12' and p2 == '12':
        print('Player 2 wins.')
    elif p1[0] == p1[-1] and p2[0] != p2[-1]:
        print('Player 1 wins.')
    elif p1[0] != p1[-1] and p2[0] == p2[-1]:
        print('Player 2 wins.')
    elif int(p1[::-1]) > int(p2[::-1]):
        print('Player 1 wins.')
    else:
        print('Player 2 wins.')
