class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        left = -1
        right = -1

        while low <= high:
            mid = (low + high)//2

            if target == nums[mid]:
                left = mid
                high = mid - 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low + high)//2

            if target == nums[mid]:
                right = mid
                low = mid + 1
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return [left, right]