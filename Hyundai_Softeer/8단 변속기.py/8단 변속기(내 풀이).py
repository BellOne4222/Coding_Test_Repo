# https://softeer.ai/practice/result.do?eventIdx=1&submissionSn=SW_PRBL_SBMS_203927&psProblemId=408#hold
# 8단 변속기
# 정렬 사용
# 정렬한 내용을 저장하고 싶으면 sorted 사용, 그냥 정렬만 할꺼면 sort 사용

import sys

dan = list(map(int, input().split()))

a = sorted(dan) 
b = sorted(dan, reverse = True)

# 숫자열 거꾸로 출력하는 법
# 1. for i in range(n, 0, -1): range(start, stop, step) -> step을 음수로 저장
# 2. for i in reversed(range(n)): reversed()는 리스트의 원소를 거꾸로 뒤집고 이를 반환하는 함수, n부터 표출되지않고 n-1부터 출력되기 때문에 print 할때는 n+1로 해야함

if dan == a:
    ans = "ascending"
elif dan == b:
    ans = "descending"
else:
    ans = "mixed"

print(ans)