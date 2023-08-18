# https://softeer.ai/practice/info.do?idx=1&eid=413
# 지도 자동 구축

import sys
import math
    

N = int(input())
zero_level = 2
for i in range(N):
    zero_level += int(math.pow(2, i)) 
    dots = int(math.pow(zero_level, 2))

print(dots)


# 0단계 : 4(2 ** 2) # 한변의 점의 개수의 제곱
# 1단계 : 9(3 ** 3)
# 2단계 : 25(5 ** 5)
# 3단계 : 81(9 ** 9)
# ...
# k단계 : (k-1단계의 제곱근 + 2 ** (k-1)) ** 2
# 위 점의 수 계산 방식을 대입하여 해결