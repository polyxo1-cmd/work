N = int(input())

a = []

for i in range(n):
    x = int(input())
    a.append(x)
a.sort()

for i in a:
    print(i)
