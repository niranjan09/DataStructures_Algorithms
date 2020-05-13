"""
list.sort vs sorted functions:
    - list.sort performs in place sorting and thereby list is changed
    - list.sort can be only used for lists and sorted can be used for any iterable
    - since sorted copies entire list and then sorts it,
        so for lists sorted is not that efficient unless its size is very large
    - both have nlogn time complexity
    - for dictionary sorted function sorts keys and returns sorted list of keys
    
"""
# To sort list of tuples
l = [(5, 2), (3, 4), (1, 4), (3, 3), (3, 2), (3, 5)]
print(sorted(l))    # works, but better to mention keys explicitly!
print(sorted(l))
l.sort(key = lambda t: t[0])
# Here, observe that, when we sort based on first element only, then 2nd elements are not sorted when 1st element is same
print(l)
# -------------------------------------------------------------------------------
def compare(x, y):
    # code written for reverse order
    # If you want normal order(increasing) then reverse the signs/symbols
    if(x<y): return 1
    elif(y<x): return -1
    else: return 0
# Import this to write your own comparator function and use it for sorting
from functools import cmp_to_key
l.sort(key = cmp_to_key(compare))
# we wrote our own comparator, for sorting in decreasing order
print(l)
#--------------------------------------------------------------------------------

