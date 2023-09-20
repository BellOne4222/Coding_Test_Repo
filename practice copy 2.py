# n = int(input())
n = 5

short = ["New","Open","Save","Save As","Save All"]


keys = []
for l in range(n):
    
    flag = False
    # option = list(input().split())
    option = list(short[l].split())
    for i in range(len(option)):
        if option[i][0] not in keys:
            keys.append(option[i][0])
            flag = True
            option[i] = "[" + option[i][0] + "]" + option[i][1:]
            break
    if not flag:
        for j in range(len(option)):
          flag = False
          for k in range(len(option[j])):
            check = option[j][k].upper()
            if check not in keys:
              keys.append(check)
              if k != len(option[j])-1:
                option[j] = option[j][:k] +"[" + option[j][k] + "]" + option[j][k+1:]
              else:
                option[j] = option[j][:k] +"[" + option[j][k] + "]"
                flag = True
                break
          if flag:
             break
    print(' '.join(option))


# option = [] # 단축키 리스트

# for i in range(n):
#     inp_list = list(short[i].split())
    
#     flag = 0 # 첫 글자가 단축키로 지정될 수 있는지
#     data = []
#     for j in range(len(inp_list)):
#         if inp_list[j][0].lower() not in option and inp_list[j][0].upper() not in option:
#             option.append(inp_list[j][0])
#             flag = 1
#             inp_list[j] = '[' + inp_list[j][0] + ']' + inp_list[j][1:]
#             break

        
#     if flag == 0: # 첫 글자가 단축키로 지정될 수 없는 경우
#         for j in range(len(inp_list)):
#             flag = 0
#             for k in range(len(inp_list[j])):
#                 if inp_list[j][k].lower() not in option and inp_list[j][k].upper() not in option:  # 단축키 설정 가능
#                     option.append(inp_list[j][k])
#                     if k != len(inp_list[j])-1:
#                         inp_list[j] = inp_list[j][:k] + '[' + inp_list[j][k] + ']' + inp_list[j][k + 1:]
#                     else:
#                         inp_list[j] = inp_list[j][:k] + '[' + inp_list[j][k] + ']'
#                     flag = 1
#                     break
#             if flag:
#                 break
#     print(' '.join(inp_list))
