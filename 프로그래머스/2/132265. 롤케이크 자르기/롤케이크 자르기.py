# 시간 복잡도: O(N)
# 공간 복잡도: O(N)

from collections import Counter

def solution(topping):
    # 정답을 저장할 변수 초기화
    answer = 0
    
    # 철수가 가진 토핑의 개수를 세는 Counter 객체 생성
    chulsu = Counter(topping)
    
    # 동생이 가진 토핑을 저장할 집합 초기화
    brother = set()
    
    # 각 토핑에 대해 반복
    for t in topping:
        # 철수의 토핑 개수 감소
        chulsu[t] -= 1
        
        # 동생이 가진 토핑 집합에 추가
        brother.add(t)
        
        # 만약 철수가 해당 토핑을 모두 사용했다면 Counter에서 제거
        if chulsu[t] == 0:
            chulsu.pop(t)
            
        # 현재까지 철수와 동생이 가진 토핑의 종류가 같다면 정답 증가
        if len(chulsu) == len(brother):
            answer += 1
            
    # 최종적으로 정답 반환
    return answer

# Counter 객체 생성: Counter를 사용하여 topping 배열의 각 토핑별 개수를 셉니다. 이를 통해 철수가 가진 토핑의 개수를 파악합니다.

# 반복문: topping 배열을 순회하면서 각 토핑에 대한 처리를 수행합니다.

# 철수의 토핑 개수를 1 감소시키고, 동생이 가진 토핑을 집합에 추가합니다.

# 만약 철수가 해당 토핑을 모두 사용했다면 Counter에서 해당 토핑을 제거합니다.

# 현재까지 철수와 동생이 가진 토핑의 종류가 같다면 정답을 증가시킵니다.

# 최종적으로 정답을 반환합니다.