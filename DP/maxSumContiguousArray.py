# Kadane's algorithm
def getMaxSumContiguousArray(arr):
    start_max, end_max, max_sum= 0, 0, float('-inf')
    start_current, end_current, current_sum  = 0, 0, float('-inf')
    for numi, num in enumerate(arr):
        if(num > current_sum + num):
            start_current = end_current = numi
            current_sum = num
        else:
            current_sum = current_sum + num
            end_current = numi
        if(current_sum > max_sum):
            start_max, end_max = start_current, end_current
            max_sum = current_sum
    return max_sum, start_max, end_max

print(getMaxSumContiguousArray([-2, -3, -5, 0, -1, -2, -3, -4]))
