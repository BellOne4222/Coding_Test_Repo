# 1204 최빈수 구하기

# 딕셔너리 get사용
T = int(input())
for i in range(T):
    num = int(input())
    li = list(map(int, input().split()))
    dic = {}

    for i in li:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 0

    # 딕셔너리 타입의 value가 가장 큰 key를 찾을 때
    # max(data, key = data.get) 
    print("#"+str(num), max(dic, key=dic.get))


#     핵심 정리🎁
# dic에서 최대 value를 갖는 key 값 찾기
# max_value_key = max(dic, key=dic.get)
 

# dic에서 key, value를 한꺼번에 출력하는 for문
# for key, value in dic.items():
# 	print(key, value)


# 내장함수 counter 사용
from collections import Counter
 
T = int(input())
for _ in range(1,T+1):
    n = int(input())
    
    li = list(map(int, input().split()))
    most_num = Counter(li).most_common()[0][0]
    print("#"+str(n),str(most_num))
 
# 1. 최빈값을 구하기위해 리스트안에 들어있는 요소들을 카운트해주는 모듈호출

# 8. Counter()함수를 이용하여 카운팅 후, 최빈값 저장