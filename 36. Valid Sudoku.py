class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        hs1 = set()
        for i in range(n):
            for j in range(n):
                if board[i][j]!="." and board[i][j] not in hs1:
                    hs1.add(board[i][j])
                elif board[i][j]!=".":
                    return False
            hs1.clear()

        hs2 = set()
        for i in range(n):
            for j in range(n):
                if board[j][i]!="." and board[j][i] not in hs2:
                    hs2.add(board[j][i])
                elif board[j][i]!=".":
                    return False
            hs2.clear()


        def loop(row_start,col_start,hs3):
            for i in range(row_start, row_start + 3):
                for j in range(col_start, col_start + 3):
                    if board[i][j]!="." and board[i][j] not in hs3:
                        hs3.add(board[i][j])
                    elif board[i][j]!=".":
                        return False
            return True

        if loop(0,0,hs3=set()) and loop(0,3,hs3=set()) and loop(0,6,hs3=set()) and loop(3,0,hs3=set()) and loop(3,3,hs3=set()) and loop(3,6,hs3=set()) and loop(6,0,hs3=set()) and loop(6,3,hs3=set()) and loop(6,6,hs3=set()):
            return True
        else:
            return False