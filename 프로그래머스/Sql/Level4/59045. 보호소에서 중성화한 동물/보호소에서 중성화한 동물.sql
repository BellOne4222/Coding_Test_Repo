/*
ANIMAL_OUTS 테이블과 ANIMAL_INS 테이블을 조인하여 보호소에서 중성화 수술을 거친 동물의 정보를 조회합니다.
*/
SELECT O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME FROM ANIMAL_OUTS AS O
JOIN ANIMAL_INS AS I ON O.ANIMAL_ID = I.ANIMAL_ID
/*
보호소에 들어올 당시에는 중성화되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 정보를 조회합니다.
*/
/*
OR 보다 AND 연산자의 우선순위가 더 높기 때문에, 괄호를 사용하여 OR 연산자를 먼저 계산하도록 합니다.
*/
WHERE
*/
WHERE 
    (I.SEX_UPON_INTAKE like 'Intact%' and O.SEX_UPON_OUTCOME like 'Neutered%') 
    OR 
    (I.SEX_UPON_INTAKE like 'Intact%' and O.SEX_UPON_OUTCOME like 'Spayed%')
/*
동물 아이디를 기준으로 오름차순으로 정렬합니다.
*/
ORDER BY ANIMAL_ID;