from itertools import permutations

# itertools 모듈에서 permutations 함수를 import합니다.
# permutations 함수는 주어진 iterable에서 가능한 모든 순열을 생성합니다.

def checkPrimeNum(num):
    # 소수를 체크하는 함수입니다.
    flag = True
    if num < 2:
        flag = False
    else:
        for i in range(2,num):
            if num % i == 0:
                flag = False
                break
    
    return flag

def solution(numbers):
    # 주어진 종이 조각으로 만들 수 있는 소수의 개수를 반환하는 함수입니다.
    
    result = 0
    
    nums = list(numbers)
    candidations = []  # 만들 수 있는 숫자 조합을 저장할 리스트
    
    for i in range(1,len(numbers)+1):  # 종이 조각의 길이만큼 반복
        for j in permutations(nums, i):  # 종이 조각의 순열을 구함
            num = ''.join(j)  # 조합된 숫자를 문자열로 변환
            if int(num) not in candidations and checkPrimeNum(int(num)):  # 중복 체크 및 소수인지 확인
                candidations.append(int(num))  # 소수라면 후보 리스트에 추가
                result += 1  # 소수이므로 결과값 1 증가
                
    return result