import math
from collections import deque

def solution(progresses, speeds):
    result = []

    progresses = deque(progresses)

    for i in range(len(progresses)):
        progresses[i] = (100 - progresses[i]) / speeds[i]
        progresses[i] = math.ceil(progresses[i])

    while progresses:

        if progresses:
            compare = progresses.popleft()
        cnt = 1
        while progresses:
            if progresses[0] <= compare:
                cnt += 1
                progresses.popleft()
            else:
                break
        result.append(cnt)

    return result