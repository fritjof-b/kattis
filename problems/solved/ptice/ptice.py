#!/Users/fritjof/anaconda3/bin/python3
# problem: ptice, rating: 1.5

names = ['Adrian', 'Bruno', 'Goran']
A = 'ABCABCABCABC' * 9
B = 'BABCBABCBABC' * 9
G = 'CCAABBCCAABB' * 9
a = b = g = 0

n = int(input())
s = input()

for i in range(n):
    if s[i] == A[i]:
        a += 1
    if s[i] == B[i]:
        b += 1
    if s[i] == G[i]:
        g += 1

winners = [(names[0], a), (names[1], b), (names[-1], g)]

winners.sort(key=lambda x:x[1], reverse=True)
print(winners[0][1])
print(winners[0][0])
for winner in winners[1:]:
    if winner[1] == winners[0][1]:
        print(winner[0])
