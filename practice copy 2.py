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
            else:
                k -= 1
                if m_standard < int(number[0]):
                    m_standard = int(number[0])

        elif m_standard >= int(number[0]):
            k -= 1
            number = number[1:]

        if k == 0:
            break
    return nums        
print(solution("4321",1))
