def parantheses(string):
    stack = []
    result = ''
    open_indices = []

    for i, char in enumerate(string):
        if char == '(':
            stack.append(i)
            result += char
            open_indices.append(len(result) - 1)
        elif char == ')':
            if stack:
                stack.pop()
                result += char
                open_indices.pop() if open_indices else None
            else:
                continue
        else:
            result += char

    for index in reversed(open_indices):
        result = result[:index] + result[index+1:]

    return result

input_string = "((a+b)-[c*d]+e"
output_string = parantheses(input_string)
print("Result:", output_string)
