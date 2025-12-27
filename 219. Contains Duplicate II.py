class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for i,no in enumerate(nums):
            if no in map and i - map[no]<=k:
                return True
            map[no] = i
            
        return False


