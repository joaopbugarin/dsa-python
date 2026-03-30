class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = (len(matrix[0]))
        rows = len(matrix)
        #the middle element of index m will sit at
        # m = matrix[m // number of columns][m % number of columns]
        l = 0
        r = rows * cols -1
        print(l,r)
        while (l <= r):
            m = (l + r) // 2
            curr_m = matrix[m // cols][m % cols]
            if curr_m == target:
                return True
            if target > curr_m:
                l = m + 1
            elif target < curr_m:
                r = m -1
        return False

sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))