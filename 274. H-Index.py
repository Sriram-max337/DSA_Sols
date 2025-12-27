#Brute Force -> Our Logic 
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        upd_citations = sorted([x for x in citations if x > 0], reverse=True)     
        if not upd_citations: 
            print(0)  
        
        n = len(upd_citations)
        Max_Hindex = 0
        
        for h in range(1, n + 1):
            count = 0
            for citation in upd_citations:
                if citation >= h:
                    count += 1
                else:
                    break 
                    
            if count >= h:
                Max_Hindex = h
            else:
                break
                
        return Max_Hindex
    
#Optmised Greedy
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        Max_Hindex=0
        
        for i in range(len(citations)):
            if citations[i]>=i+1:
                Max_Hindex = i+1
        
        return Max_Hindex