A = int(input())
B = int(input())

ones = B % 10
tens = (B // 10) % 10
hundreds = B // 100

print(A * ones)
print(A * tens)
print(A * hundreds)
print(A*B)
