#Our logic -> Brute Force -> Semi Optimised
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n 
            x = 1/x  
    
        pow = 1
        if n == 0:
            pow = 1
        else:
            if n % 2 == 0:
                pow = (x**(n//2))**2
            else:
                pow = x * ((x**(n//2))**2)

        return pow