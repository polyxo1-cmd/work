N, X = input().split()
N = int(N)
X = int(X)

numbers = input().split()

for num in numbers:
    if int(num) < X:
        print(num, end=' ')
