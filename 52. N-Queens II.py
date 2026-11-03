class Solution:
    def totalNQueens(self, n: int) -> int:
        rows = cols = n
        x = 0
        def NQ(rem_queens, used_cols, placed):
            nonlocal x
            if rem_queens == 0:
                x += 1 
                return

            for col in range(cols):
                if col in used_cols:
                    continue

                conflict = False
                for (r,c) in placed:
                    if (abs((n-rem_queens) - r) == abs(col - c)):
                        conflict = True
                        break
                if conflict:
                    continue

                NQ(rem_queens-1, used_cols | {col}, placed + [((n-rem_queens),col)])

        NQ(n,set(),[])
        return x