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
        anagrams = defaultdict(list)
        for word in strs:
            key = "".join(
                sorted(word)
            )  # sorted returns a list, we need to join to convert back to string
            anagrams[key].append(word)
        return list(anagrams.values())


solution = Solution()
print(solution.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
