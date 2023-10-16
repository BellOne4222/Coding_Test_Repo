# 함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고, D는 첫 번째 수를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
# 함수는 조합해서 한 번에 사용할 수 있다. 예를 들어, "AB"는 A를 수행한 다음에 바로 이어서 B를 수행하는 함수이다. 예를 들어, "RDD"는 배열을 뒤집은 다음 처음 두 수를 버리는 함수이다.

import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    operation = list(map(str,sys.stdin.readline().rstrip()))
    n = int(sys.stdin.readline())
    lst = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    if n == 0:
        lst = deque()

    flag = True
    for i in operation:
        if i == 'R':
            lst.reverse()
        elif i == 'D':
            if lst:
                lst.popleft()
            else:
                print("error")
                flag = False
                break
    if flag == 0:
        print("["+",".join(lst)+"]")

