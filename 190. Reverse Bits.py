class Solution:
    def reverseBits(self, n: int) -> int:
        org_bin = format(n, "032b")
        rev_int = int(org_bin[::-1], 2)

        return rev_int