import math

def is_palindrome_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0: 
        return False
    original = n
    reversed_num = 0
    temp = n
    while temp > 0:
        reversed_num = reversed_num * 10 + temp % 10
        temp //= 10
    
    if original != reversed_num:
        return False
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    
    return True
