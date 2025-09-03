#square = 1^2 + 9^2 = 82
#square = no -> 82
#square = 8^2 + 2^2 = 68
#square = no ->68
#square = 6^2 + 8^2 = 100
#square = 1^2 + 0^2 + 0^2 = 1 -> Stop and the no is a Happy No

#Optimised -> Using Hashing
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n!=1 and n not in seen:
            seen.add(n)
            square_sum = 0
            temp = n

            while temp > 0:
                digit = temp%10
                square_sum+=digit**2
                temp//=10
            n = square_sum

        return n==1