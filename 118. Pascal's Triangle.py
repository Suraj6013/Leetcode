from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        pascal = [[1]] 
        for i in range(1, numRows):
            row = [1]  
            for j in range(1, i):                
                row.append(pascal[i-1][j-1] + pascal[i-1][j])
            row.append(1)  
            pascal.append(row)
        
        return pascal        
solution = Solution()
print(solution.generate(5))