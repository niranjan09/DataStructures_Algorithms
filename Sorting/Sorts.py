import time

def swap(arr, i , j):
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp

def selection_sort(arr):
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if(arr[i] > arr[j]):
				swap(arr, i, j)
	return arr

def bubble_sort(arr):
	swapped = True
	while(swapped == True):
		swapped = False
		for i in range(len(arr)-1):
			if(arr[i] > arr[i+1]):
				swap(arr, i, i+1)
				swapped = True
	return arr

def insertion_sort(arr):
	for i in range(1, len(arr)):
		if(arr[i] < arr[i-1]):
			temp = i-1
			print arr[i], arr[temp], arr
			while(arr[i] < arr[temp] and temp>=0):
				print "shifting...", arr[i], arr[temp]
				temp-=1
			arr.insert(temp+1, arr[i])
			del arr[i+1]
	return arr

def merge_sort(arr):
	arr_len = len(arr)
	if(arr_len == 1):
		return arr
	a = merge_sort(arr[:arr_len/2])
	b = merge_sort(arr[arr_len/2:])
	c = []
	i_a = i_b = 0
	a_len = len(a)
	b_len = len(b)
	while(i_a < a_len and i_b < b_len):
		if(a[i_a]<b[i_b]):
			c.append(a[i_a])
			i_a+=1
		else:
			c.append(b[i_b])
			i_b+=1
	if(i_a < a_len):
		for remaining in a[i_a:]:
			c.append(remaining)
	if(i_b < b_len):
		for remaining in b[i_b:]:
			c.append(remaining)
	return c

def quick_sort(arr):
	if(len(arr)<1):
		return arr
	pivot = arr[len(arr) // 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	return quick_sort(left) + middle + quick_sort(right)
	
def direct_addressing_sort(arr):
	maximum = max(arr)
	minimum = min(arr)
	
	a = len(range(minimum, maximum+1))*[0]
	
	for i in range(len(arr)):
		a[i]+=1
	
	print a
	

print(time.time())
print(quick_sort([-2.2, -2.2, -2.2]*5+[1.1]*5))
print(time.time())
