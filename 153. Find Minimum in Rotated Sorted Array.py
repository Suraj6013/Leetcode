from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        if nums[left] <= nums[right]:
            return nums[left]
            
        while left <= right:
            mid = (left + right) // 2          
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return nums[left]
solution = Solution()
print(solution.findMin([3,4,5,1,2]))