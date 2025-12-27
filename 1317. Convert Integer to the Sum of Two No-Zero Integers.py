class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        no1,no2=0,0
        i=0
        for x in range(int(n)):
            if '0' not in str(0+i) and '0' not in str(n-i):
                no1=0+i
                no2=n-i
            else:
                i+=1

        return no1,no2
    
    