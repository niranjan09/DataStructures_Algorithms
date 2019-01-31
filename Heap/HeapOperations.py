def MaxHeapify(A, i, num_nodes = 4):
	largest = i
	for node in range(num_nodes):
		if((num_nodes*i+node+1)<len(A) and A[num_nodes*i+node+1] > A[largest]):
			largest = num_nodes*i+node+1
	if(largest != i):
		temp = A[i]
		A[i] = A[largest]
		A[largest] = temp
			
		MaxHeapify(A, largest, num_nodes)
	


def BuildMaxHeap(A, num_nodes = 4):
	for i in range((len(A)-1)//num_nodes, -1, -1):
		MaxHeapify(A, i, num_nodes)

def HeapMaximum(A):
	return A[0]

def HeapExtractMax(A, num_nodes = 4):
	max_num = A[0]
	A[0] = A[len(A) - 1]
	A.pop(len(A)-1)
	MaxHeapify(A, 0, num_nodes)
	return max_num

def HeapIncreaseKey(A, i, key, num_nodes = 4):
	A[i] = key
	while i>0 and A[(i-1)//num_nodes]<A[i]:
		temp = A[i]
		A[i] = A[(i-1)//num_nodes]
		A[(i-1)//num_nodes] = temp
		i = (i-1)//num_nodes

def MaxHeapInsert(A, key, num_nodes = 4):
	A.insert(len(A), -9999)
	HeapIncreaseKey(A, len(A)-1, key, num_nodes)


A = [6, 77, 11, 21, 60, 15, -2, 16, 91, 90]
BuildMaxHeap(A, 2)
print(A)
HeapExtractMax(A, 2)
print(A)
MaxHeapInsert(A, 91, 2)
print(A)
