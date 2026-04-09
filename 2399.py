n = int(input())
a = list(map(int, input().split()))

a.sort()

answer = 0

for i in range(n):
    answer += a[i] * (2 * i - n + 1)

print(answer * 2)
