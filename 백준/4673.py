def d(n):
    return n + sum(map(int, str(n)))

created = set()

for i in range(1, 10001):
    created.add(d(i))

for i in range(1, 10001):
    if i not in created:
        print(i)
