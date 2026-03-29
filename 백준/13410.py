N, K = map(int, input().split())

max_num = 0

for i in range(1, K+1):
    num = N * i
    rev = int(str(num)[::-1])
    
    if rev > max_num:
        max_num = rev
        
print(max_num)
