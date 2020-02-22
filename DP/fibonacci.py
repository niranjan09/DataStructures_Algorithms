from functools import lru_cache

import sys
# By default system's recusion limit is not sufficient, so setting it to appropriate value
sys.setrecursionlimit(10**6)

@lru_cache(maxsize = None)
def nthFibonacciModmRecusion(n, m):
    return n%m if n<2 else (nthFibonacciModmRecusion(n-1, m) + nthFibonacciModmRecusion(n-2, m))%m

# returns cycle with fibo series mod m
def getFiboModmCycle(m):
    cycle = [0, 1, 1]
    if m==1:
        return [0]
    while(not(cycle[-1] == 1 and cycle [-2]==0)):
        cycle.append((cycle[-1]+cycle[-2])%m)
    return cycle[:-2]
    

if '__main__' == __name__:
    #print(nthFibonacciModmRecusion(10000, 10**9+7))
    #for mi in range(2, 100):
    #    print(len(getFiboModmCycle(mi)))
    print(len(getFiboModmCycle(10**7)))
