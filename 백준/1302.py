n = int(input())

books = {}

for _ in range(n):
    name = input()
    
    if name in books:
        books[name] += 1
    else:
        books[name] = 1

max_count = max(books.values())

result = []

for name in books:
    if books[name] == max_count:
        result.append(name)

result.sort()

print(result[0])
