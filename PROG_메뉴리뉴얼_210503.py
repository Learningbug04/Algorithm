from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    counter = defaultdict(int)
    order_set_list = []
    unique_menu = set()
    answer = []
    for order in orders:
        order_set_list.append(set(order))
        unique_menu.update(set(order))
        for menu in order:
            counter[menu] += 1
    for i in range(2,11):
        for check_menu in list(combinations(unique_menu,i)):
            cnt = 0
            for menu in order_set_list:
                check_menu = set(check_menu)
                print(check_menu.intersection(menu))
                # if len(check_menu.intersection(menu)) >=2:
                #     cnt +=1
            if cnt >=2 :
                answer.append(check_menu)
    print(answer)
    # return answer