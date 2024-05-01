# grade = [3,2,1,2]
grade = [2,2,1]

sorted_grade = sorted(grade, reverse=True)

grade_dict = {}

cur_grade = 1

student = 0

highest_grade = sorted_grade[0]

result = []

for i in range(len(grade)):
    if sorted_grade[i] == highest_grade:
        student += 1
    else:
        cur_grade += student
        student = 1
        highest_grade = sorted_grade[i]

    if sorted_grade[i] not in grade_dict:
        grade_dict[sorted_grade[i]] = cur_grade

for j in range(len(grade)):
    result.append(grade_dict[grade[j]])

print(result)
