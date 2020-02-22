
"""
Rabin-Karp algorithm for pattern searching
Assumption: pattern and text contains only small english letters a to z.
For better performance use optimal power function
"""
def rabin_karp(text, pattern):
    PRIME = 10013236879455627894
    BASE = 26
    current_hash = 0
    pattern_hash = 0
    ans = []
    for i in range(len(pattern)):
        current_hash += (BASE**i)*(ord(text[i]) - ord('a'))
        pattern_hash += (BASE**i)*(ord(pattern[i]) - ord('a'))
    if(current_hash == pattern_hash):
        ans.append(0)
    for i in range(len(pattern), len(text)):
        current_hash -= (ord(text[i - len(pattern)]) - ord('a'))
        current_hash /= BASE
        current_hash += ((ord(text[i]) - ord('a'))*BASE**(len(pattern)-1))
        if current_hash == pattern_hash and text[i-len(pattern)+1: i+1] == pattern:
            ans.append(i - len(pattern) + 1)
    return ans


if '__main__' == __name__:
    text = 'abcdghebcdacdabcdshabcdghebcdacdabcdsh'
    pattern = 'abcd'
    print(rabin_karp(text, pattern))
