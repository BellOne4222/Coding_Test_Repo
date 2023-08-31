# 앞의 예제 테스트 케이스는 다 맞았으나 뒤의 케이스에서는 25점..


def solution(number, k):
    m_standard = 0
    a = 0
    nums = []

    for i in range(len(number)):

        if len(nums) == 0:
            if int(number[i]) > m_standard:
                m_standard = int(number[i])
            nums.append(number[i])
            number = number[1:]
        elif m_standard < int(number[0]):
            if int(nums[-1]) < int(number[0]):
                a = nums.pop()
                k -= 1
                if int(a) > m_standard:
                    m_standard = int(a)
                nums.append(number[0])
                number = number[1:]
            elif int(nums[-1]) == int(number[0]):
                nums.append(number[0])
                number = number[1:]
            elif int(nums[-1]) > int(number[0]):
                nums.append(number[0])
                number = number[1:]
            else:
                k -= 1
                if m_standard < int(number[0]):
                    m_standard = int(number[0])

        elif m_standard >= int(number[0]):
            k -= 1
            number = number[1:]

        if k == 0:
            break
    
    answer = ''
    for j in nums:
        answer += j
    return answer + number     
print(solution("4177252841",4))
# print(solution("4321",1))

# 25점...
# 테스트 1 〉	통과 (0.03ms, 10.4MB)
# 테스트 2 〉	실패 (0.03ms, 10.5MB)
# 테스트 3 〉	실패 (0.10ms, 10.5MB)
# 테스트 4 〉	실패 (0.08ms, 10.5MB)
# 테스트 5 〉	실패 (0.34ms, 10.4MB)
# 테스트 6 〉	통과 (14.50ms, 10.5MB)
# 테스트 7 〉	실패 (25.70ms, 10.5MB)
# 테스트 8 〉	실패 (122.66ms, 10.6MB)
# 테스트 9 〉	실패 (5.00ms, 11.7MB)
# 테스트 10 〉	실패 (3134.72ms, 12.2MB)
# 테스트 11 〉	통과 (0.02ms, 10.4MB)
# 테스트 12 〉	실패 (0.02ms, 10.5MB)
