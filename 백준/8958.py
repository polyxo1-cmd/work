n = int(input())

for i in range(n):
    ox_list = input()
    total_score = 0
    current_score = 0
    
    for ox in ox_list:
        if ox == 'O':
            current_score += 1
            total_score += current_score
            
        else:
            current_score = 0
        
    print(total_score)
