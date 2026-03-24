max = 0
person = 0
for i in range(4):
    a,b = map(int,input().split())
    person +=(b-a)
    if max < person:
        max = person
print(max)
