# https://velog.io/@tiiranocode/Python-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8A%9C%ED%94%8C 참고

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"

lst = sorted([s.split(',') for s in s[2:-2].split('},{')], key=len)

result = []

for i in lst:
    for j in i:
        if int(j) not in result:
            result.append(int(j))
            break

print(result)