# 필수로 배워야 하는 스킬을 담는 deque를 만들어서 필수 스킬을 배울때 마다 popleft 해서 순서에 안맞으면 break하고 다음 스킬 트리로 넘어가는 로직이고, 
# 중간에 필수 스킬에 없는 스킬은 cnt만 증가시켜 cnt가 스킬 트리의 길이와 같아지면 가능한 스킬트리 이므로 available 변수를 1 증가 시켜서 총 가능한 스킬 트리 개수 반환하는 로직


from collections import deque

def solution(skill, skill_trees):
    essential_skills = [i for i in skill]
    essential_skill = deque(essential_skills)
    skill_sequence = [j for j in range(len(skill))]
    skill_dict = dict(zip(essential_skill,skill_sequence))
    available = 0
    cnt = 0
    
    for j in skill_trees:
        cnt = 0
        essential_skills = [i for i in skill]
        essential_skill = deque(essential_skills)
        for k in j:
            if k not in skill_dict:
                cnt += 1
            elif k == essential_skill[0]:
                cnt += 1
                essential_skill.popleft()
            else:
                break
        if cnt == len(j):
            available += 1
    return available

# print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))