from typing import List, Optional, Dict, Set, Tuple, Union
import heapq
import collections
from collections import defaultdict, deque, Counter, OrderedDict
import bisect
import math


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        values_count = [[] for i in range(len(nums) + 1)]
        # ^ array that contains in the position i an array of numbers
        # that appears i times. we first count how many times that
        # number appears and then put it in this array
        for num in nums:
            count[num] = 1 + count.get(
                num, 0
            )  # creating a hashmap {number: number Count}
        for value, times in count.items():  # .items() return key:value pair
            values_count[times].append(value)

        res = []
        print("values count:", values_count)
        for i in range(len(values_count) - 1, 0, -1):
            for n in values_count[i]:
                res.append(n)
                if len(res) == k:
                    return res


solution = Solution()
print(solution.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))
