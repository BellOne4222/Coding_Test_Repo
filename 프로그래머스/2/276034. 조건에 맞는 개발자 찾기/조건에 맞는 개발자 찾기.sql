-- DEVELOPERS 테이블에서 Python이나 C# 스킬을 가진 개발자의 정보를 조회합니다.
SELECT 
    ID, -- 개발자의 ID를 선택합니다.
    EMAIL, -- 개발자의 이메일을 선택합니다.
    FIRST_NAME, -- 개발자의 이름을 선택합니다.
    LAST_NAME -- 개발자의 성을 선택합니다.
FROM 
    DEVELOPERS
WHERE 
    -- 개발자의 스킬 코드(SKILL_CODE)에서 Python이나 C# 스킬을 가지고 있는지 확인합니다.
    -- Python과 C#의 코드 값을 합하여 해당 스킬을 가지고 있는지 확인합니다.
    SKILL_CODE & 
    (SELECT SUM(CODE) FROM SKILLCODES WHERE NAME IN ('Python', 'C#'))
    -- 비트 AND 연산 결과가 0이 아니면 해당 스킬을 가지고 있는 것입니다.
    <> 0
ORDER BY 
    ID; -- ID를 기준으로 오름차순으로 결과를 정렬합니다.