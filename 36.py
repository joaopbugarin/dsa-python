class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, row in enumerate(board):  # pylint: disable=consider-using-enumerate
            col = [board[n][i] for n in range(len(board))]
            filtered_row = [x for x in row if x.isdigit()]
            filtered_col = [x for x in col if x.isdigit()]

            if len(filtered_row) != len(set(filtered_row)) or len(filtered_col) != len(
                set(filtered_col)
            ):
                return False

        for box_row in [0, 3, 6]:  # Starting rows for boxes
            for box_col in [0, 3, 6]:  # Starting columns for boxes
                box = []
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        box.append(board[row][col])
                filtered_box = [x for x in box if x.isdigit()]
                print(box)
                if (len(filtered_box)) != len(set(filtered_box)):
                    return False
        print("#######################################")
        return True


sol = Solution()

print(
    sol.isValidSudoku(
        [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
print(
    sol.isValidSudoku(
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
    )
)
