from typing import List, Optional, Dict, Set, Tuple, Union
import heapq
import collections
from collections import defaultdict, deque, Counter, OrderedDict
import bisect
import math

# create a hashmap with the letter count for each word
# if the word has a same letter count, push them together into the new array


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = []
        result = []

        def count_letters_loop(words: str) -> Dict[str, int]:
            for word in words:
                count.append(count_letters(word))
            return count

        def count_letters(word: str) -> Dict[str, int]:
            letters = {}
            for letter in word:
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
            return letters

        anagrams = []
        for i in count_letters_loop(strs):
            for j in strs:
                if count_letters(j) == i:
                    anagrams.append(j)
            result.append(anagrams)
            anagrams = []

        return result


solution = Solution()
print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
