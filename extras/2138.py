from typing import List, Optional, Dict, Set, Tuple, Union
import heapq
import collections
from collections import defaultdict, deque, Counter, OrderedDict
import bisect
import math


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        arr = []
        j = 0
        print(len(s) // k)
        for i in range(len(s) // k):
            value = s[j : j + k]
            j += k
            arr.append(value)
        print("mod: ", len(s) % k)
        mod = len(s) % k
        if mod:
            complete = str(s[-mod::]) + (k - mod) * fill
            arr.append(complete)
        return arr


solution = Solution()
print(solution.divideString(s="ctoyjrwtngqwt", k=8, fill="n"))
