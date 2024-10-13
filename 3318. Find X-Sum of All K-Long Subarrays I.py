from typing import List
from collections import Counter

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        n = len(nums) - (k - 1)
        
        for i in range(n):
            subarray = nums[i:i + k]
            y = {}
            
            for num in subarray:
                if num in y:
                    y[num] += 1
                else:
                    y[num] = 1
            
            # Sort by frequency (descending) and by value (descending)
            sorted_elements = sorted(y.items(), key=lambda item: (-item[1], -item[0]))
            
            # Keep only the top x most frequent elements
            top_x_elements = sorted_elements[:x]
            
            # Calculate the sum of the resulting array
            x_sum = sum(element for element, freq in top_x_elements)
            
            result.append(x_sum)
        
        return result

solution = Solution()
print(solution.findXSum([1,1,2,2,3,4,2,3], 6, 2))  # Example usage