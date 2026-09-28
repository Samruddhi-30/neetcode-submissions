class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            new = [num for num in row if num!='.']
            if len(new)!=len(set(new)):
                return False

        col =[]
        for i in range(0,9):
            curr = []
            for j in range(0,9):
                curr.append(board[j][i])
            col.append(curr)

        for row in col:
            new = [num for num in row if num!='.']
            if len(new)!=len(set(new)):
                return False

        return True
        