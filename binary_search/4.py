class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array for efficiency
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total = m + n
    half = total // 2  # How many elements should be on the left

    # Binary search on nums1
    left, right = 0, m

    while left <= right:
        i = (left + right) // 2  # Partition position in nums1
        j = half - i              # Partition position in nums2

        nums1_left = nums1[i-1] if i > 0 else float('-inf')
        nums1_right = nums1[i] if i < m else float('inf')
        nums2_left = nums2[j-1] if j > 0 else float('-inf')
        nums2_right = nums2[j] if j < n else float('inf')

        # Check if partition is valid
        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            # Valid partition found!
            # Calculate median based on odd/even total length
            if total % 2 == 1:
                # Odd: return max of left side
                return max(nums1_left, nums2_left)
            else:
                # Even: return average of max(left) and min(right)
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2

        elif nums1_left > nums2_right:
            # nums1 partition too far right, search left half
            right = i - 1
        else:
            # nums1 partition too far left, search right half
            left = i + 1