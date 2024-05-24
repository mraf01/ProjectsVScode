'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
write a function to determine if the input string is valid.

An input string is valid if: 

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

For example:

Test:
print(is_valid_parenthesis("()"))   Result: True

print(is_valid_parenthesis("(]"))   Result: False
'''

def is_valid_parenthesis(s):
    l = []
    diz = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in diz.values():
            l.append(char)
        elif char in diz.keys():
            if l == [] or diz[char] != l.pop():
                return False
    return l == []

# Test
print(is_valid_parenthesis("()"))
print(is_valid_parenthesis("(]"))