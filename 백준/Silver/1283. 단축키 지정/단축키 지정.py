n = int(input())  # 입력으로 정수 n을 받음

keys = []  # 사용된 첫 글자를 추적하기 위한 리스트

# n번 반복하며 옵션을 처리
for l in range(n):
    flag = False  # 옵션에 대한 처리 결과를 나타내는 플래그
    option = list(input().split())  # 공백을 기준으로 옵션을 분리하여 리스트로 저장

    # 옵션 내의 단어들을 순회하면서 처리
    for i in range(len(option)):
        # 만약 해당 단어의 첫 글자가 keys 리스트에 없는 경우 (소문자 또는 대문자로 구분)
        if option[i][0].lower() not in keys and option[i][0].upper() not in keys:
            keys.append(option[i][0])  # keys 리스트에 첫 글자를 추가
            flag = True  # 처리 플래그를 True로 설정
            option[i] = "[" + option[i][0] + "]" + option[i][1:]  # 해당 단어의 첫 글자를 대괄호로 감싸줌
            break  # 처리가 완료되면 루프 종료

    # 처리 플래그가 False인 경우 (첫 글자가 keys 리스트에 이미 존재)
    if not flag:
        for j in range(len(option)):
            flag = False
            for k in range(len(option[j])):
                # 단어 내의 글자들을 순회하면서 처리
                if option[j][k].lower() not in keys and option[j][k].upper() not in keys:
                    keys.append(option[j][k])  # keys 리스트에 해당 글자를 추가
                    if k != len(option[j]) - 1:
                        option[j] = option[j][:k] + "[" + option[j][k] + "]" + option[j][k + 1:]
                    else:
                        option[j] = option[j][:k] + "[" + option[j][k] + "]"
                    flag = True  # 처리 플래그를 True로 설정
                    break  # 처리가 완료되면 루프 종료

            if flag:
                break

    # 처리된 옵션을 공백을 기준으로 분리된 문자열로 변환하여 출력
    print(' '.join(option))