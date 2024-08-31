import sys
import heapq

def solution(n, data):
    student = {}  # 학생들의 추천 횟수를 저장하는 딕셔너리

    # 추천된 학생 번호 리스트인 data를 순회
    for s in data:
        if s not in student:  # 학생이 아직 사진틀에 없는 경우
            if len(student) >= n:  # 사진틀이 꽉 찬 경우
                # 추천 횟수가 가장 적은 학생을 찾는다
                a = heapq.nsmallest(min(student), student, key=student.get)
                student.pop(a[0])  # 해당 학생을 사진틀에서 제거

            student[s] = 1  # 새로운 학생을 사진틀에 추가하고, 추천 횟수를 1로 설정
        else:
            student[s] += 1  # 이미 사진틀에 있는 학생이라면 추천 횟수를 증가시킴

    # 최종적으로 사진틀에 남아 있는 학생들의 번호를 오름차순으로 정렬하여 반환
    return sorted(student.keys())

# 입력 처리
n = int(sys.stdin.readline().rstrip())  # 사진틀의 개수
r = int(sys.stdin.readline().rstrip())  # 총 추천 횟수
data = list(map(int, sys.stdin.readline().split()))  # 추천된 학생 번호 리스트

# 결과 출력
print(*solution(n, data))  # solution 함수로부터 반환된 학생 번호를 출력
