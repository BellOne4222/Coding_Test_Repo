# 문제 접근 : topping의 길이가 최악의 경우에는 10^6이므로 시간 복잡도를 O(N)으로 맞춰야 풀이가 가능했다.
# 철수(형)에게 모든 토핑을 몰아주고, 하나씩 동생한테 주면서 그때마다의 토핑 가지수를 비교하여 같으면 경우의수를 하나씩 늘려가는 로직 설계
# 시간 복잡도 : O(N)
# 시간 복잡도를 맞추기 위해서는 topping에 관한 리스트를 만드는 과정을 한번만 해야 되고 리스트 내의 원소를 처리하는 과정과 비교하는 과정의 시간 복잡도를
# O(1)으로 맞춰야 해결이 가능하다. 그래서 내장함수 counter를 사용해서 토핑 종류에 대한 개수를 딕셔너리 형태로 만들고 동생한테 add로 하나씩 주면서, 종류의 개수가 0이 되면 종류를 삭제하여 불필요한 반복을 없앴다.
# 토핑 종류의 수가 같아지면 경우에수 1 증가시켜서 결과 반환

from collections import Counter

def solution(topping):
    elder = Counter(topping)
    
    younger = set()
    case = 0
    
    for i in topping:
        younger.add(i)
        elder[i] -= 1

        if elder[i] == 0:
            del elder[i]
        if len(younger) == len(elder):
            case += 1

    return case


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))