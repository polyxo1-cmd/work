k, l = map(int, input().split())

students = {}

for i in range(l):
    num = input()
    students[num] = i

result = sorted(students.items(), key=lambda x: x[1])

for i in range(min(k, len(result))):
    print(result[i][0])
