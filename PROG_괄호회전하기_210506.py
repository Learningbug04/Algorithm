parentheses_dict = {'[':']' , '{':'}', '(':')'}

def solution(s):
    if len(s) % 2:
        return 0
    answer = 0
    str_list = [x for x in s]
    for i in range(len(s)):
        for j in range(int(len(s)/2)):
            str_list = verify_string(str_list)
            if str_list == False:
                break
            if str_list == '':
                print(s)
                answer += 1
                break
        s = s[1:] + s[0]
        str_list = [x for x in s]
    return answer

def verify_string(str_list):
    next_parentheses = parentheses_dict.get(str_list[0],False)
    if str_list[1] == next_parentheses:
        if len(str_list) == 2:
            return ''
        return str_list[2:]
    if str_list[-1] == next_parentheses:
        if len(str_list) == 2:
            return ''
        return str_list[1:-1]
    return False