from typing import List, Optional, Dict, Set, Tuple, Union
import heapq
import collections
from collections import defaultdict, deque, Counter, OrderedDict
import bisect
import math


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        matches = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in matches:
                stack.append(char)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if matches[opening] != char:
                    return False

        return len(stack) == 0


x = 1 + 2
solution = Solution()
print(solution.isValid(s="([])"))
print(solution.isValid(s="()[]{}"))
print(solution.isValid(s="(("))
print(solution.isValid(s="){"))
print(solution.isValid(s="()))"))
