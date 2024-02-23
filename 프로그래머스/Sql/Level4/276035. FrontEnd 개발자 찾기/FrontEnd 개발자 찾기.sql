# JOIN
/*
SKILLCODES 테이블과 DEVELOPERS 테이블을 조인하여 Front End 스킬을 가진 개발자의 정보를 조회합니다.
*/
SELECT DISTINCT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM
  SKILLCODES
  JOIN DEVELOPERS ON CODE & SKILL_CODE 
  /*
    비트 연산자 &를 사용해서 비트단위 AND연산을 수행 -> CODE와 SKILL_CODE의 이진 표현에서 각 자릿수를 비교하고 둘 다 1인 경우에만 결과를 1로 반환
     각 비트는 특정 스킬을 나타내며, 해당 스킬이 있으면 1, 없으면 0으로 표시됩니다.
    */
/*
SKILLCODES 테이블의 CATEGORY가 'Front End'인 스킬에 대한 정보를 조회합니다.
*/
WHERE CATEGORY = 'Front End'
/*
조회된 결과를 개발자의 ID를 기준으로 오름차순으로 정렬합니다.
*/
ORDER BY ID;

# 서브쿼리
/*
DEVELOPERS 테이블에서 Front End 스킬을 가진 개발자의 정보를 조회합니다.
*/
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
/*
SKILLCODES 테이블에서 CATEGORY가 'Front End'인 스킬들의 코드를 합산하여,
해당 코드들을 가진 개발자를 조회합니다.
*/
WHERE SKILL_CODE & (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'Front End')
/*
개발자의 ID를 기준으로 오름차순으로 정렬합니다.
*/
ORDER BY ID;