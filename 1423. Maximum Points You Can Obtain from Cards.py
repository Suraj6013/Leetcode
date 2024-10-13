from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        current_sum = sum(cardPoints[:k])
        max_sum = current_sum
        
        for i in range(1, k + 1):
            current_sum = current_sum - cardPoints[k - i] + cardPoints[-i]
            max_sum = max(max_sum, current_sum)
            
        return max_sum

solution = Solution()
print(solution.maxScore([1, 2, 3, 4, 5, 6, 1], 3))  # Example usage