def pow(n, m, MOD = 2**31 - 1):
    ans = 1
    while m:
        #print(ans)
        if m & 1:
            ans *= n
            ans %= MOD
        m >>= 1
        n *= n
        n %= MOD
        
    return ans
    
print(pow(9, 12))
