-- DEVELOPERS 테이블(D)에서 개발자들의 정보를 조회합니다.
SELECT
    -- CASE 문을 사용하여 각 개발자의 GRADE를 정의합니다.
    CASE 
        -- 개발자의 SKILL_CODE에 Python 스킬과 Front End 스킬이 모두 존재하는 경우, 'A' 등급으로 설정합니다.
        WHEN EXISTS (SELECT S.CODE FROM SKILLCODES S WHERE S.CODE & D.SKILL_CODE AND S.NAME = 'Python')
             AND EXISTS (SELECT S.CODE FROM SKILLCODES S WHERE S.CODE & D.SKILL_CODE AND S.CATEGORY = 'Front End') THEN 'A'
        -- 개발자의 SKILL_CODE에 C# 스킬이 존재하는 경우, 'B' 등급으로 설정합니다.
        WHEN EXISTS (SELECT S.CODE FROM SKILLCODES S WHERE S.CODE & D.SKILL_CODE AND S.NAME = 'C#') THEN 'B'
        -- 개발자의 SKILL_CODE에 Front End 스킬이 존재하는 경우, 'C' 등급으로 설정합니다.
        WHEN EXISTS (SELECT S.CODE FROM SKILLCODES S WHERE S.CODE & D.SKILL_CODE AND S.CATEGORY = 'Front End') THEN 'C'
        -- 그 외의 경우에는 NULL을 반환합니다.
        ELSE NULL
    END AS GRADE,
    D.ID,
    D.EMAIL
FROM 
    DEVELOPERS D
-- GRADE가 NULL이 아닌 경우에만 필터링합니다.
HAVING 
    GRADE IS NOT NULL
-- GRADE와 ID를 기준으로 오름차순으로 정렬합니다.
ORDER BY 
    GRADE, ID;