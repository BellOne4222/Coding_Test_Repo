/*
ONLINE_SALE 테이블과 USER_INFO 테이블을 조인하여 2021년에 가입한 전체 회원들 중 상품을 구매한 회원수와 상품을 구매한 회원의 비율을 구합니다.
*/
SELECT 
    YEAR(O.SALES_DATE) AS YEAR, 
    MONTH(O.SALES_DATE) AS MONTH, 
    /*
    2021년에 가입한 회원 중 해당 월에 상품을 구매한 회원 수를 COUNT 함수와 DISTINCT를 이용하여 구합니다.
    */
    COUNT(DISTINCT U.USER_ID) AS PURCHASED_USERS,
    /*
    2021년에 가입한 전체 회원 수를 구하는 서브쿼리를 이용하여 해당 월에 상품을 구매한 회원의 비율을 구합니다.
    */
    ROUND(COUNT(DISTINCT U.USER_ID) / (SELECT COUNT(*) FROM USER_INFO WHERE JOINED LIKE '2021%'), 1) AS PURCHASED_RATIO
FROM ONLINE_SALE AS O
JOIN USER_INFO AS U ON O.USER_ID = U.USER_ID
/*
2021년에 가입한 회원만을 조회합니다.
*/
WHERE U.JOINED LIKE '2021%'
/*
년, 월 별로 그룹화하여 결과를 출력합니다.
*/
GROUP BY YEAR, MONTH
/*
년을 기준으로 오름차순으로 정렬하고, 년이 같은 경우 월을 기준으로 오름차순으로 정렬합니다.
*/
ORDER BY YEAR ASC, MONTH ASC;

-- 풀이
-- 문제를 읽으면서 조건들을 분리하며 이해해 본다.

-- 2021년 가입한 정체 회원, 상품 구매 이력이 있는 회원,

-- 상품 구매 회원의 비율 ( 2021 가입, 구매 이력 회원 / 2021가입, 전체 회원)

-- 그리고 이것들을 년, 월 별로 출력을 해야 하니 그룹을 묶어줘야겠다.

-- 우선 user table과 online table을 user_id로 join을 시킨 뒤 where절로 2021년 가입한 회원들만 추려준다.
-- 문제에서 원하는 년도와 월은 DATE_FORMAT()을 이용하여 추출한 뒤 column명을 year, month로 지정하여 나중에 group by (column명)을 깔끔하게 해 준다.
-- 년, 월별로 그룹을 묶어준 뒤 해당 월에 구입한 회원 총 수를 count()를 이용해 구해준다.
-- (주의) join 된 테이블 결과는 한 회원이 여러 번 구매 이력이 있을 수 있기 때문에 distinct를 이용하여 중복 회원 id를 제거해 준 뒤 count를 세줘야 한다.
-- 상품 구매 회원 비율을 구하기 위해 2021년에 가입한 총 회원 수를 구해줘야 된다.
-- (SELECT COUNT(*) FROM USER_INFO WHERE joined LIKE '2021%') 서브 쿼리를 이용해 간단하게 구해준다.
-- 문제에서 둘째 자리에서 반올림을 해줘야 하기 때문에 round() 이용해 준다.
-- 문제에서 원하는 대로 order by
-- Round() 함수에서 ex) round(0.1234, 2)는 소수점 둘째 자리까지 반올림을 하는 의미이다. 문제에서는 소수점 둘째 자리에서 반올림을 해야 하기 때문에, 첫째 자리까지 반올림한다는 의미로 이해할 수 있다.