class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# sorting algorithm -> O(n logn)
# could use a hashmap instead

solution = Solution()
print(solution.isAnagram("anagram", t="nagaram"))
