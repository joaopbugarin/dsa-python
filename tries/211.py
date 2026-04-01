class WordDictionary: #bruteforcing first, will redo in 1-2 days optimised

    def __init__(self):
        self.words = []

    def addWord(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        for w in self.words:
            if len(w) != len(word):
                continue

            for i in range(len(word)):
                if w[i] != word[i] and word[i] != '.':
                    break
            else:  # FOR/ELSE, PYTHON MAGIC
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)