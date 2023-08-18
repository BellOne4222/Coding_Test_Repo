# 짝수 홀수 개수

def solution(num_list):
    even = []
    odd = []
    for i in num_list:
        if i % 2 == 0:
            even.append([i]) #append는 여러 수를 넣지 못하므로, i라는 문자열을 추가시켜준다.
        else:
            odd.append([i])
    answer = [len(even), len(odd)]
    return answer