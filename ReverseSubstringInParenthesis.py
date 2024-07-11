# Reverse Substrings Between Each Pair of Parenthesis
## Given s that only consists of lowercase english letters and brackets
## Reverse substring inside each matching parenthesis
## Result should not include the brackets

# Example 
## Input: s = (u(love)i)
## Output: iloveu


def reverse_parentheses_stack(s):#Using a stack approach
    stack = []
    for char in s:
        if char == ')':
            substr =[]
            while stack and stack[-1] != '(':
                substr.append(stack.pop())
            stack.pop()  # pop the '('
            stack.extend(substr)
        else:
            stack.append(char)
    return ''.join(stack)


# Example usage
s = "(ed(et(oc))el)"
result = reverse_parentheses_stack(s)
print(result) 



