from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for i in nums[:]:
            if i == 0:
                nums.remove(i)
                count += 1
        for _ in range(count):
            nums.append(0)
        print(nums)
solution = Solution()
solution.moveZeroes([0, 0, 1]) # [1, 0, 0]
