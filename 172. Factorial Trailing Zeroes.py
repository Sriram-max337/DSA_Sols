#our logic -> Brute Force ,Unoptimised
import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        fac = math.factorial(n)
        count=0
        for i in range(fac):
            if fac%10 == 0:
                count+=1
                fac//=10
            else:
                break

        return count
    
