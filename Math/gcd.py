def gcd(a, b):
    while(a!=b):
        if(a>b): a = a%b if a%b else b
        else: b = b%a if b%a else a
    return a

assert gcd(4, 12) == 4
assert gcd(39, 81) == 3

# Using built in methods
import math
print(math.gcd(4, 12))
print(math.gcd(39, 81))
