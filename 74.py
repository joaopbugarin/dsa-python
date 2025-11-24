class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_len = (len(matrix[0]))
        matrix_len = len(matrix)
        print(row_len, matrix_len)
        l = 0
        r = row_len - 1 + row_len * (matrix_len - 1)
        m = (l + r) // 2
        print(l,m,r)

sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))