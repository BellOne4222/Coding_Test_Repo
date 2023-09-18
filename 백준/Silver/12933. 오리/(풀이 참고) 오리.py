# all(iterable) 함수는 인자로 받은 반복 가능한 자료형(iterable)의 모든 요소가 참(True)이면 참(True)을 반환하는 함수 입니다.
# any(iterable) 함수는 인자로 받은 반복가능한 자료형(iterable)중 단 하나라도 참(True)이 있으면 참(True)를 반환하는 함수 입니다. 반대로 모든 요소가 거짓(False)인 경우에만 거짓(False)을 반환합니다.
# https://velog.io/@gilyeon00/%EB%B0%B1%EC%A4%80-12933%EB%B2%88-%EC%98%A4%EB%A6%AC-python-%EC%8B%A4%EB%B2%843?ref=codenary 참고

sound = list(input())
ans = 0

# sound 문자열의 시작이 q가 아니거나 문자열 끝이 k가 아니거나 문자열의 길이가 5의 배수가 아니면 -1반환하고 프로그램 종료
if sound[0] != "q"  or  sound[-1] != "k" or len(sound) % 5 :
    print(-1)
    exit()

def find_quack(start) :
    quack = "quack"
    j = 0
    global ans 
    new_ori = True # 새로운 오리로 생성하라는 flag
    for i in range(start, len(sound)): # q를 발견한 인덱스 부터 문자열의 길이 만큼 반복
        if sound[i] == quack[j]: # input으로 받은 문장의 인덱스와 quack 문자열의 인덱스를 따로 움직이면서 같은지 확인
            if sound[i] == "k":
                if new_ori:     # 새로운 오리일 경우, 오리(ans) 추가
                    ans += 1
                    new_ori = False  # k값으로 끝났으니 새로운 오리를 생성하지 말라는 flag          
                j = 0 # 이어지는 "q" 탐색 -> 새로운 오리가 아님 (현재 오리)
                sound[i] = 0           
                continue        
            j += 1 # 두 문자열의 각 자리가 같으면 다음 인덱스로 넘긴다.
            sound[i] = 0 # 같은 자리의 sound 문자열 문자는 0으로 바꾼다.


for i in range(len(sound) - 4):# 어차피 q 뒤에는 무조건 uack이 와야하므로 -4를 해준다
    if sound[i] == "q" : # q를 발견하면 find_quack 함수 실행
        find_quack(i)


if any(sound) or ans == 0 : # sound 문자열 중 True이거나 오리 개수가 0이면 -1 반환
    print(-1)
else :
    print(ans)