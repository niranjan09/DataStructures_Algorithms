def quick_select(arr, k):
	if(len(arr)<=1):
		return arr[0]
	pivot = arr[len(arr) // 2]
	left = [x for x in arr if x < pivot]
	middle = [x for x in arr if x == pivot]
	right = [x for x in arr if x > pivot]
	l = len(left)
	m = len(middle)
	r = len(right)
	if(l>=k):
		return quick_select(left, k)
	elif (l+m)>=k:
		return middle[k-l-1]
	else:
		return quick_select(right, k-l-m)

class Node:
	def __init__(self):
		self.char = ''
		self.childNodes = {}

class Trie:
	def __init__(self):
		self.root = Node()
	def insertChar(self, word):
		current_node = self.root
		currentChar = 0
		wordlen = len(word)
		while word[currentChar] in current_node.childNodes and currentChar<wordlen:
			current_node = current_node.childNodes[word[currentChar]]
			currentChar+=1
		if currentChar<wordlen:
			while currentChar<wordlen:
				nextNode = Node()
				current_node.childNodes[word[currentChar]] = nextNode
				current_node = nextNode
				currentChar+=1
	def printit(self, node):
		for child in node.childNodes.keys():
			print child
			self.printit(node.childNodes[child])

trie = Trie()
trie.insertChar("apple")
trie.printit(trie.root)
