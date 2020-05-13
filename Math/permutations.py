def getCombinations(n):
    ans = []
    for i in range(1<<n):
        ans.append([int(x) for x in list(format(i, '0'+str(n)+'b'))])
    return ans

def getPermutations(n):
    if len(n) == 1:
        return [n]
    ans = []
    nc = list(set(n))
    for ni in nc:
        i = n.index(ni)
        n.pop(i)
        #print(n)
        for n1permi in getPermutations(list(n)):
            #print(n1permi)
            n1permi.append(ni)
            ans.append(n1permi)
        n.insert(i, ni)
    #print(ans)
    return ans
           
print(getPermutations([1, 1, 1]))
#print(getCombinations(3))
