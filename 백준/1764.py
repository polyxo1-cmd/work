n, m = map(int, input().split())

not_heard = set()

for _ in range(n):
    name = input()
    not_heard.add(name)

result = []

for _ in range(m):
    name = input()
    
    if name in not_heard:
        result.append(name)

result.sort()

print(len(result))

for name in result:
    print(name)
