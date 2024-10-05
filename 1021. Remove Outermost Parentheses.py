class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        depth = 0

        for char in s:
            if char == '(':
                if depth > 0:
                    result.append(char)
                depth += 1
            elif char == ')':
                depth -= 1
                if depth > 0:
                    result.append(char)

        return ''.join(result)

solution = Solution()
print(solution.removeOuterParentheses("(()())(())"))