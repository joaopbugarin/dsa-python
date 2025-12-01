from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_num = defaultdict(int)
        elements = [[] for _ in range(len(nums)+1)]
        for num in nums:
            count_num[num] += 1
        for num, times in count_num.items():
            elements[times].append(num)
        print(count_num)
        print(elements)
        top_app = []
        pushed = 0
        for i in range(len(elements)-1,0,-1):
            for num in elements[i]:
                top_app.append(num)
                pushed += 1
                if pushed == k:
                    return top_app


sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2))
print(sol.topKFrequent([1],1))