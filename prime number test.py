﻿num = 15
if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print('not a prime number')
            break
    else:
        print('prime number')
        
