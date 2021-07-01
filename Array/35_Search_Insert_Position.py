class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         i = 0
#         while i < len(nums) and target > nums[i]:
#             i += 1
        
#         return i
    # def searchInsert(self, nums: List[int], target: int) -> int:
        
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + int((right-left)/2)

            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return right + 1
