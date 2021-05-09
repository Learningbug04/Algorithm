from itertools import combinations
from collections import Counter

def solution(orders, courses):
    answer = []
    unique_order = set()
    temp = []
    for course in courses:
        for order in orders:
            combi = combinations(sorted(order), course)
            temp.extend(list(combi))
        counter = Counter(temp)
        most_counter = counter.most_common(1)
        if len(most_counter) > 0 and most_counter[0][1] > 1:
            max_value = most_counter[0][1]
            answer.extend([''.join(x[0]) for x in list(counter.items()) if x[1] == max_value])
        temp = []
    return sorted(answer)
