class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        max_freq = 0
        res = []
        for num in nums:
            count[num] += 1
            max_freq = max(max_freq, count[num])

        bucket = [[] for _ in range(max_freq+1)]
        for value in count:
            bucket[count[value]].append(value)


        j = max_freq
        while k > 0 and j > 0:
            if bucket[j]:
                res += bucket[j]
            k -= len(bucket[j])
            j -= 1

        return res