s = input()
p = input()

if len(s) > len(p) + 1:
    print('No')
elif s == p or p.swapcase() == s or (p == s[0:-1] and s[-1].isdigit()) or (p == s[1:] and s[0].isdigit()):
    print('Yes')
else:
    print('No')
