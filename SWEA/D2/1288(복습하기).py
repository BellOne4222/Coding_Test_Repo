# 1288 새로운 불면증 치료법

T = int(input())
for i in range(1, T+1):
    N = int(input())
    k = 0 # 곱해주는 수
    
    nums = [str(i) for i in range(0,10)] # 0~9까지의 숫자 리스트
    while nums: 
        k += 1 # k를 1씩 증가시키면서 N에 곱해준다.
        num = N * k
        num = str(num) # 밑에서 반복문 돌리기 위해 str로 자료형 변경
        
        for j in num:
            if j in nums:
                nums.remove(j) # 0~9라는 숫자가 나올때마다 nums의 숫자를 지워서 없어지면 while문 탈출해서 
    print("#{} {}".format(i, num)) # 호석이가 양을 센 횟수느 xN번 이므로 양을 센 횟수인 num 반환