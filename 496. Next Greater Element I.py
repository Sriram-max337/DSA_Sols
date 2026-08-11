class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        stack.append(nums2[0])
        HM = {}
        for i in range(1,len(nums2)):
            while stack and stack[-1] < nums2[i]:
                poped_ele = stack.pop()
                HM[poped_ele] = nums2[i]
            stack.append(nums2[i])

        for j in range(len(stack)):
            HM[stack[j]] = -1
            
        ans = []
        for k in range(len(nums1)):
            ans.append(HM[nums1[k]])

        return ans