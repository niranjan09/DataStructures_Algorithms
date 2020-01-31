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
l = [(5, 2), (3, 4), (1, 4)]
print(sorted(l))    # works, but better to mention keys explicitly!
print(sorted(l))
l.sort(key = lambda t: t[0])
print(l)

