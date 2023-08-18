# 시간 초과 직전 가까스로 solve...
# deque 사용해서 원형 방식을 popleft로 맨 앞 숫자를 빼서 맨 뒤에 append하는 방식으로 구현
# itertools.islice(arr,0,i)를 통해 deque를 0부터 i만큼 잘라서 합을 sums 배열에 넣고 중복 제거를 위해서 set처리를 해서 중복 제거 후 배열의 길이 반환

# itertools.islice : https://daewoonginfo.blogspot.com/2019/04/python-collections-deque-itertools.html 참고
# sys.setrecursionlimit(1000000) : https://fuzzysound.github.io/sys-setrecursionlimit 참고 : 시간 초과 때문에 실행 시간을 줄이기 위해 사용


from collections import deque
import itertools
import sys
sys.setrecursionlimit(1000000) # 기본 재귀 깊이는 1000이므로 얕아서 재귀깊이를 10**6으로 깊이 만들어 시간 초과 해결

def solution(elements):
    arr = deque(elements)
    sums = []
    for i in range(1, len(elements)+1): # 길이가 1부터 배열의 길이까지 증가하며 크기만큼의 합을 구함
        for j in range(len(elements)): 
            sum_arr = sum(list(itertools.islice(arr,0,i))) # islice를 이용해서 deque slice : 리스트는 index로 slice가 가능하지만 deque은 silce를 islice로 해야해서 islice 사용
            sums.append(sum_arr) # 해당 크기만큼 자른 배열의 합을 sums에 저장
            a = arr.popleft() # 맨 앞 배열 원소를 빼서 배열 맨 뒤에 넣기(원형 배열 구현)
            arr.append(a)
    
    result = list(set(sums)) # 중복 제거
    
    return len(result) # 결과 배열의 길이 반환

    
        
    
    
            
        
    
        

    