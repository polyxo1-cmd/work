t = int(input())

for i in range(t):
    s = input()
    a = []
    ok = True

    for x in s:
        if x == '(':
            a.append(x)
        else: 
            if len(a) == 0:
                ok = False
                break
            else:
                a.pop()

    if len(a) != 0:
        ok = False

    if ok:
        print("YES")
    else:
        print("NO")
