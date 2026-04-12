class TrieNode():
    def __init__(self):
        self.children = {}
        self.wordsEnd = set()

class Trie ():
    def __init__(self, words):
        self.root = TrieNode()
        if words:
            for word in words:
                self.addWord(word)

    def addWord (self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.wordsEnd.add(word)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words_trie = Trie(words)

        sol = set()
        seen = set()

        def findWord(m,n, node):
            if (m,n) in seen:
                return
            if m < 0 or m >= len(board):
                return
            if n <0 or n >= len(board[m]):
                return

            curr_char = board[m][n]
            if curr_char not in node.children:
                return

            node = node.children[curr_char]

            if node.wordsEnd:
                for word in node.wordsEnd:
                    sol.add(word)

            seen.add((m,n))
            findWord(m,n+1, node)
            findWord(m,n-1, node)
            findWord(m+1,n, node)
            findWord(m-1,n, node)
            seen.remove((m,n))

        for m in range(len(board)):
            for n in range(len(board[m])):
                findWord(m,n, words_trie.root)

        return list(sol)