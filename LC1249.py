def parantheses(string):
    stack = []
    result = ''
    
    for char in string:
        if char == '(':
            stack.append(char)
            result += char
        elif char == ')':
            if stack:
                stack.pop()
                result += char
            else:
                return "Unbalanced parentheses"
        elif char == '[' or char == ']':

            continue
        else:
            result += char
    
    if stack:
        return "Unbalanced parentheses"
    else:
        return result

input_string = "((a+b)-[c*d]+e"
output_string = parantheses(input_string)
print("Result:", output_string)
