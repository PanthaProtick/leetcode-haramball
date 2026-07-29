class TrieNode(object):
    def __init__(self):
        self.children={}
        self.eow=False

class WordDictionary(object):

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur=self.root
        for char in word:
            if char not in cur.children:
                cur.children[char]=TrieNode()
            cur=cur.children[char]
        cur.eow=True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        def dfs(j, root):
            cur=root
            
            for i in range(j,len(word)):
                c=word[i]

                if c=='.':
                    for child in cur.children.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur=cur.children[c]
            return cur.eow
        return dfs(0,self.root) 


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)