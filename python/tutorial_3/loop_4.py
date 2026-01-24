# Reverse a number using loop (e.g., input 123 → output 321).

num = 123
result = 0

# last_digit = num %10    # 3
# num = num // 10         # 12
# result = (result * 10)+last_digit # 0*10 + 3

# last_digit = num %10    # 2
# num = num // 10         # 1
# result = (result * 10)+last_digit # 3*10 + 2 = 32

# last_digit = num %10    # 1
# num = num // 10         # 0
# result = (result * 10)+last_digit # 32*10 + 1 = 321



while num>0:
    last_digit = num %10    
    num = num // 10         
    result = (result * 10)+last_digit 
    
print(result)

