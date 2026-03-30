class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #k is => 1 but <= highest pile
        #.ceil(pile//k) == (pile + k - 1) // pile
        l = 1
        r = max(piles)
        while l <= r:
            k = (l+r)//2
            total_time = 0
            for pile in piles:
                time = (pile + k -1) // k
                total_time += time
            if total_time <= h:
                r = k - 1
            else:
                l = k + 1
        return l

sol = Solution()
print(sol.minEatingSpeed([3,6,7,11],8))
print(sol.minEatingSpeed([30,11,23,4,20],5))
print(sol.minEatingSpeed([30,11,23,4,20],6))