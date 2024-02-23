/*
REST_REVIEW 테이블과 MEMBER_PROFILE 테이블을 조인하여 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회합니다.
*/
SELECT M.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') FROM REST_REVIEW AS R
JOIN MEMBER_PROFILE AS M ON R.MEMBER_ID = M.MEMBER_ID
/*
서브쿼리를 사용하여 리뷰를 가장 많이 작성한 회원의 MEMBER_ID를 조회합니다.
*/
WHERE M.MEMBER_ID = (
    SELECT MEMBER_ID 
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    ORDER BY COUNT(*) DESC
    LIMIT 1
) 
/*
리뷰 작성일을 기준으로 오름차순으로 정렬하고, 리뷰 작성일이 같다면 리뷰 텍스트를 기준으로 오름차순으로 정렬합니다.
*/
ORDER BY REVIEW_DATE ASC, REVIEW_TEXT ASC;