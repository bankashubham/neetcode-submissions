class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True
    
    def search(self, word: str) -> bool:
        def dfs(node, index):
            if not node:
                return False

            if index == len(word):
                return node.endOfWord

            char = word[index]
            if char != ".":
                if char not in node.children:
                    return False
                return dfs(node.children[char], index + 1)

            else:
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False

        
        return dfs(self.root, 0)
