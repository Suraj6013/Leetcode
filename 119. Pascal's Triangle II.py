from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]

        pascal = [[1]]
        for i in range(1, rowIndex + 1):
            row = [1]
            for j in range(1, i):
                row.append(pascal[i-1] [j-1] + pascal[i-1][j])
            row.append(1)  
            pascal.append(row)
        return pascal[rowIndex]  

solution = Solution()
print(solution.getRow(5)) 