class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        ans = []

        for i in range(len(nums1)):
            heapq.heappush(heap, (nums1[i]+nums2[0],i,0))

        while len(ans) < k:
            ele = heapq.heappop(heap)
            ans.append([nums1[ele[1]],nums2[ele[2]]])
            if ele[2] + 1 < len(nums2):
                heapq.heappush(heap, (nums1[ele[1]]+nums2[ele[2]+1],ele[1],ele[2]+1))

        return ans