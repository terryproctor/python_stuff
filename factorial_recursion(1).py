﻿# Recursive implementation of the factorial function
def factorial(n):
    if n == 1:    # the base case (termination condition)
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(4)) # 4 * 3 * 2 * 1 = 24