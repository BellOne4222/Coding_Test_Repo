# 2063 중간값 찾기

N = int(input())
# map 형식으로 저장(int형으로 모든 값을 저장하는데 input().split()을 통해 띄워쓰기 되어 있으면 분리) 후 리스트로 만듬
numbers = list(map(int, input().split()))
numbers.sort()                              # 오름차순으로 정렬
# 중간값은 총길이/2 +1인데, 배열은 0부터 시작이니 +1 안해도 됨
answer = numbers[N//2] # 개수 // 2를 인덱스로 그 인덱스의 숫자 출력하는 방식
print(answer)