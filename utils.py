def fibonacci(n):

    if n <= 0:
        raise ValueError("n must be positive")

    if n == 1:        
        return 0

    if n == 2:
         return 1


    a, b = 0, 1

    for _ in range(2, n):
         a, b = b, a + b


    return b

def is_power_of_five(n):
    if n < 1:
        return False
    while n % 5 == 0:
        n //= 5
    return n == 1
