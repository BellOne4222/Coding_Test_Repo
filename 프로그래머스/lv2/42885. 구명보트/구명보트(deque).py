# popleft를 사용하기 위해 deque를 사용을 했고, people을 정렬을 하고, 가장 무게가 무거운 사람을 빼서 이 사람과 같이 탈 수 있는 사람이 있는지 없는지 검사를 해서 없으면 보트 하나 증가 시키고, 
# 보트 최대 무게에서 무거운 사람의 무게를 뺀 값이 가장 가벼운 사람보다 크거나 같으면 둘 다 보트에 태워서 deque에서 제거하여 보트 개수 반환하는 로직

from collections import deque

def solution(people, limit):
    people = deque(sorted(people)) # deque 정렬
    boat = 0

    while people:
        High_Weight = people.pop() # 가장 무거운 사람 pop
        another_person = limit - High_Weight # 같이 보트에 탈 수 있는 사람의 무게를 보트 최대 무게 - 가장 무거운 사람의 무게
        if people and (another_person >= people[0]): # 보트에 같이 탈수 있으면
            people.popleft() # 둘 다 deque에서 제거하고 보트 수 1 증가
        
        boat += 1 # 혼자만 탑승 가능하면 보트 수 1 증가
        
    return boat

print(solution([70, 50, 80, 50], 100))