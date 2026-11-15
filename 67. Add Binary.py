class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin_int = int(a, 2) + int(b, 2)

        return format(bin_int, 'b')