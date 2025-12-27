class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1_upd = []
        for i in range(m):
            nums1_upd.append(nums1[i])
    
        newarr = sorted(nums1_upd + nums2)

        for i in range(len(newarr)):
            nums1[i] = newarr[i]

#One liner        
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2[:n])