sound = list(input())
ans = 0

if sound[0] != "q"  or  sound[-1] != "k" or len(sound) % 5 :
    print(-1)
    exit()

def find_quack(start) :
    quack = "quack"
    j = 0
    global ans 
    new_ori = True      # 새로운 오리로 생성하라는 flag
    for i in range(start, len(sound)):
        if sound[i] == quack[j]:
            if sound[i] == "k":
                if new_ori:     # 새로운 오리일 경우, 오리(ans) 추가
                    ans += 1
                    new_ori = False     # k값으로 끝났으니 새로운 오리를 생성하지 말라는 flag          
                j = 0           # 이어지는 "q" 탐색 - 새로운 오리가 아님 (현재 오리)
                sound[i] = 0           
                continue        
            j += 1
            sound[i] = 0


for i in range(len(sound) - 4):     # 어차피 q 뒤에는 무조건 uack이 와야하므로 -4를 해준다
    if sound[i] == "q" :
        find_quack(i)


if any(sound) or ans == 0 :
    print(-1)
else :
    print(ans)