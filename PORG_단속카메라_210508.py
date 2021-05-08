def solution(routes):
    routes.sort(key=lambda x:x[1])
    length = len(routes)
    answer = 1
    max_out = routes[0][1]
    for i in range(1,length):
        if routes[i][0] <= max_out:
            continue
        answer += 1
        max_out = routes[i][1]
    return answer