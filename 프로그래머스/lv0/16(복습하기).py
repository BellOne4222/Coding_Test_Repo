# 배열 원소의 길이

def solution(strlist):
    answer = [len(i) for i in strlist]
    return answer

# 이름으로 이루어진 리스트를 이름의 길이로 리스트 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)