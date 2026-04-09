k = int(input())
nums = []

for i in range(k):
    x = int(input())
    
    if x == 0:
        nums.pop()
        
    else:
        nums.append(x)
        
print(sum(nums))
