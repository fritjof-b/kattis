#!/Users/fritjof/anaconda3/bin/python3
# problem: hangman, rating: 1.6
secret = set(input())
t = set()
guesses = input()
w = 0

for guess in guesses:
    t.add(guess)
    if guess not in secret:
        w += 1
    if w == 10:
        break

if secret.issubset(t):
    print('WIN')
else:
    print('LOSE')
