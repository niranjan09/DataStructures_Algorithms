# returns index of number just lesser/equal than num
def binarySearchCeilIndex(arr, start, end, num):
    print(start, end)
    if end == start:
        if arr[start] >= num:
            return start
        elif arr[start] < num:
            return min(start + 1, len(arr) - 1)
    else:
        mid = (start + end)//2
        if(arr[mid] == num):
            return mid
        elif arr[mid] < num:
            return binarySearch(arr, mid + 1, end, num)
        else:
            return binarySearch(arr, start, mid, num)

arr = [2, 3, 5, 7, 9, 10, 18, 101]
arr1 = [10, 11]
print(binarySearch(arr1, 0, len(arr1) - 1, 12))
