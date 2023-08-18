# 3809. 화섭이의 정수 나열 

# 화섭이는 다음과 같은 흥미로운 추측에 대해 들었다.

# “모든 정수는 π = 3.14159265…의 어떤 연속한 부분으로 나타난다.”

# 화섭이는 π에 대해 이것을 테스트해 보기는 힘들다고 생각했고, 그냥 유한한 정수열에 대해서 위처럼 연속한 부분을 끊어내어 보았다.

# 예를 들면 “3 0 1”같은 정수열로는 3, 0, 1, 30, 301을 만들 수 있다.

# 화섭이는 주어진 정수열로 만들 수 없으면서 가장 작은 정수가 무엇인지 궁금해졌다.

# 이를 구하는 프로그램을 작성하라. 위의 예에서는 0, 1은 나타나지만 2는 나타나지 않으므로 2가 답이 된다.

# 두 번째 테스트케이스를 예로 들면,


# 위 그림과 같이 0부터 11까지의 정수는 만들 수 있으나 12를 만들 수 없다. 그러므로 12가 답이 된다.


# [입력]

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스의 첫 번째 줄에는 N(1 ≤ N ≤ 103)이 주어진다.

# 다음으로는 N개의 정수 d1, d2, …, dN (0 ≤ di ≤ 9)이 순서대로 주어진다.

# d들은 공백 하나 또는 줄바꿈으로 구분되어 있다.


# [출력]

# 각 테스트 케이스마다 만들어낼 수 없는 가장 작은 정수를 출력한다.

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    d=[]
    d.extend(list(input().split()))
    d.join(d)
    
    
    for i in range(int(d)):
        if str(i) not in d:
            print("#{} {}".format(test_case, i))
            break

tc = int(input())
 
for t in range(1, tc + 1):
    n = int(input())
    nums = ''
    while True:
        nums += ''.join(map(str, input().split()))
        if len(nums) == n:
            break
    ans = 0
    while str(ans) in nums:
        ans += 1
    print("#{} {}".format(test_case, ans))

# 숫자 한글자씩 되있는거 문자열 숫자로 만드는법
# while len(d)<N:
#         d.extend(list(input().split()))
#     d=''.join(d)