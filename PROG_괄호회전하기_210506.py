from collections import defaultdict

parentheses_dict = {'[':']' , '{':'}', '(':')'}

def solution(s):
    answer = 0
    for i in range(len(s)):
        if verify_parentheses(s) is True:
            answer += 1
        s = s[1:] + s[0]
    return answer

def verify_parentheses(string):
    stack = []
    if string[0] == '}' or string[0] == ']' or string[0] == ')':
        return False
    for i in range(len(string)):
        if len(stack) == 0:
            stack.append(string[i])
            continue
        poped_stack = stack.pop()
        if parentheses_dict.get(poped_stack,'') == string[i]:
            continue
        stack.append(poped_stack)
        stack.append(string[i])
    if len(stack) == 0:
        return True
    return False
        
        
    