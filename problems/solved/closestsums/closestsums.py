#!/Users/fritjof/anaconda3/bin/python3
# problem: closestsums, rating: 2.8

k = 1
try:
    while True:
        n = int(input())
        ints = []
        queries = []
        for _ in range(n):
            ints.append(int(input()))

        m = int(input())
        for _ in range(m):
            queries.append(int(input())) 

        ints.sort()
        print(f"Case {k}:")
        for query in queries:
            c = int(1e6)
            for i in ints:
                for j in ints[ints.index(i) + 1:]:
                    if abs(i + j - query) < abs(c - query):
                        c = i + j

            print(f'Closest sum to {query} is {c}.')
        k += 1

except EOFError as e:
    pass
