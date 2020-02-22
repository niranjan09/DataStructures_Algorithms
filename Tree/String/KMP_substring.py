def KMP_substring_search(s, p):
    plen = len(p)
    pp, tmi = [0]*plen, 0
    for pi in range(1, plen):
        if(p[pi] == p[tmi]):
            tmi += 1
            pp[pi] = tmi
        else:
            while(tmi):
                tmi = pp[tmi - 1]
                if(p[tmi] == p[pi]):
                    tmi += 1
                    pp[pi] = tmi
                    break
    slen, tmi, ans = len(s), 0, []
    for si in range(slen):
        if(s[si] == p[tmi]):
            tmi += 1
        else:
            while(tmi):
                tmi = pp[tmi - 1]
                if(s[si] == p[tmi]):
                    tmi += 1
                    break
        if(tmi == plen):
            ans.append(si - plen + 1)
            tmi = pp[tmi - 1]
    return ans

if __name__ == "__main__":
    s = 'aaaaaaaa'
    p = 'a'
    print(KMP_substring_search(s, p))
                
