#Optmised but lil messy and long
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5,'X':10,'L':50,"C":100,"D":500,"M":1000}
        special_nos = ["IV","IX","XL","XC","CD","CM"]
        sum = 0 
        i = 0
       
        while i < len(s):
            if i + 1 < len(s) and s[i] + s[i+1] in special_nos:
                if s[i] == "I" and s[i+1] == "V":
                    sum += 4
                    i += 2
                elif s[i] == "I" and s[i+1] == "X":
                    sum += 9
                    i += 2
                elif s[i] == "X" and s[i+1] == "L":
                    sum += 40
                    i += 2
                elif s[i] == "X" and s[i+1] == "C":
                    sum += 90
                    i += 2
                elif s[i] == "C" and s[i+1] == "D":
                    sum += 400
                    i += 2
                elif s[i] == "C" and s[i+1] == "M":
                    sum += 900
                    i += 2
            else:
                digit = roman[s[i]]
                sum += digit 
                i += 1
        
        return sum  
    
#Optmised Core Roman logic
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I':1, 'V':5,'X':10,'L':50,"C":100,"D":500,"M":1000}
        special_nos = ["IV","IX","XL","XC","CD","CM"]
        sum = 0 
        n="MCMXCIV"
        
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                sum-=roman[s[i]]
            else:
                sum+=roman[s[i]]
        
        return sum