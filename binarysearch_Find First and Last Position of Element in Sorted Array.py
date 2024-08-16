from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        first = findFirst(nums, target)
        last = findLast(nums, target)

        if first <= last and first < len(nums) and nums[first] == target:
            return [first, last]
        else:
            return [-1, -1]

solution = Solution()
print(solution.searchRange([5, 7, 7, 8, 8, 10], 8))