from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        output = []
        x = 0
        y = 1
        for i in range(len(nums)):
            if nums[i] > 0:
                output.insert(x, nums[i])
                x+=2
            else:
                output.insert(y, nums[i])
                y+=2
        return output

solution = Solution()
print(solution.rearrangeArray([1, 2, 3, -4, -1, 4]))