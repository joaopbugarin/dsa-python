from typing import List, Optional, Dict, Set, Tuple, Union
import heapq
import collections
from collections import defaultdict, deque, Counter, OrderedDict
import bisect
import math


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elements = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in elements:
                return [index, elements[diff]]
            else:
                elements[num] = index


solution = Solution()
print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
