def solution(routes):
    routes.sort()
    camera = 0
    start = routes[0][0]
    end = routes[0][1]
    for i in range(1, len(routes)):
        if start <= routes[i][0] <= end:
            camera += 1
            start = routes[i][0]
            if start > end:
                start, end = end, start
        else:
            start = routes[i][0]
            end = routes[i][1]
    return routes