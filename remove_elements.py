import ast
class Solution:
    def removeElement(self, nums, val):
        k = 0
        i = 0  
        while i < len(nums): 
            if nums[i] == val:
                nums.pop(i)  
                nums.append("_")
            else:
                k += 1 
        print(k)
        print(nums)

nums_input = input()
try:
    nums = ast.literal_eval(nums_input)
    if not isinstance(nums, list):
        raise ValueError
except (SyntaxError, ValueError):
    print("Invalid input. Please enter a list.")
    exit()

val = int(input())

obj = Solution()
result = obj.removeElement(nums, val)