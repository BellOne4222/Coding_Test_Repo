# 참고 : https://yuna0125.tistory.com/154
# 중복순열을 이용 (product)
# for문을 돌려서 반복 횟수(i)가 1부터 5일때까지 가능한 단어들의 조합을 다 만들고 words 배열에 넣어준다. (이때, [AA, AAA, AAAA] 이런 식으로 합쳐서 보기 위해 ''.join 해줘야 함)
# 사전순으로 정렬하기 위해서 words 배열을 sort (오름차순 정렬) 
# words 배열에서, 매개변수로 주어진 word에 해당하는 index에 1을 더한 값 리턴 (배열의 인덱스는 0부터 시작하므로)


from itertools import product

def solution(word):
    arr = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    for i in range(1, 6):
        for pr in product(arr, repeat = i): # repeat는 조합할 숫자의 숫자
            words.append(''.join(pr))   
    
    words.sort()
    return words.index(i) + 1