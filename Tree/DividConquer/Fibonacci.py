import sys
sys.path.insert(1, '../')
import math
from Math.matrixOperations import multiplyMatrix


MOD = 2**31 - 1
def getNthFibonacciModM(n, m = MOD):
    f = [[[1, 1], [1, 0]]]
    ans = [[1, 0], [0, 1]]
    n-=1
    nl = int(math.log2(n)+1)
    for i in range(1, nl):
        nf = multiplyMatrix(f[-1], f[-1])
        for i in range(2):
            for j in range(2):
                nf[i][j]%=m
        f.append(nf)
    print(nl, f)
    ci = 1<<nl
    while nl>=0:
        if(ci&n):
            ans = multiplyMatrix(ans, f[nl])
            for i in range(2):
                for j in range(2):
                    ans[i][j]%=m

        ci//=2
        nl-=1
    return ans[0][0]

if '__main__' == __name__:
    print(getNthFibonacciModM(36, 10**6))
