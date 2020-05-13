# Code to generate one number from another;
# The only operations permissible are *2 and -1.
d = {}
def solution(n, m):
    #print(n, m)
    if((n, m) in d):
        return (d[(n, m)])
    if(n<=0):
        return 11111
    if(n>=m):
        return n - m
    d[(n, m)] = 11111
    l = solution(n-1, m)
    r = solution(2*n, m)
    ans = 1+min(l, r)
    d[(n, m)] = ans
    return ans

print(solution(3, 5))
