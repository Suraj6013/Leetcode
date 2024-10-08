class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            x = nums.pop(len(nums)-1)
            nums.insert(0, x)

solution = Solution()
solution.rotate([1,2,3,4,5,6,7], 3)