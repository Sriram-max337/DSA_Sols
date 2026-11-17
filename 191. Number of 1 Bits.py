class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_str = format(n, "b")

        return bin_str.count("1")