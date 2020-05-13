class Trie:
    class TrieNode:
        def __init__(self, char = None):
            self.char = char
            self.nextchar = {}
            self.endcnt = 0

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.TrieNode('@')
    
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        nextNode = self.root
        for char in word:
            if not nextNode.nextchar.get(char, None):
                nn = self.TrieNode(char)
                nextNode.nextchar[char] = nn
            nextNode = nextNode.nextchar.get(char)
        nextNode.endcnt += 1
        
    def printTrie(self, node = None):
        if not node:
             node = self.root
        print("the current char is:", node.char)
        for nc in node.nextchar:
            self.printTrie(node.nextchar[nc])

if __name__=='__main__':
    t = Trie()
    t.insert('trying')
    t.insert('tri')
    t.insert('triangularly')
    t.printTrie()
