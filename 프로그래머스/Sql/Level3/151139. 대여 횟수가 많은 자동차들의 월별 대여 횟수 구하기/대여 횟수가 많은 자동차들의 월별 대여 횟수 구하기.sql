-- CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 대여 시작일을 기준으로 2022년 8월부터 2022년 10월까지 총 대여 횟수가 5회 이상인 자동차들에 대해서
SELECT 
    MONTH(START_DATE) AS MONTH, -- 대여 시작일을 월로 추출하여 MONTH라는 이름의 열로 선택합니다.
    CAR_ID, -- 자동차 ID를 선택합니다.
    COUNT(*) AS RECORDS -- 각 자동차 ID의 대여 횟수를 카운트하여 RECORDS라는 이름의 열로 선택합니다.
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE 
    DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10' -- 대여 시작일이 2022년 8월부터 2022년 10월까지인 대여 기록을 선택합니다.
    AND CAR_ID IN (
        SELECT 
            CAR_ID 
        FROM 
            CAR_RENTAL_COMPANY_RENTAL_HISTORY 
        WHERE 
            DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10' -- 대여 시작일이 2022년 8월부터 2022년 10월까지인 대여 기록 중에서
        GROUP BY 
            CAR_ID 
        HAVING 
            COUNT(CAR_ID) >= 5 -- 해당 자동차의 총 대여 횟수가 5회 이상인 자동차 ID를 선택합니다.
    )
GROUP BY 
    CAR_ID, MONTH -- 자동차 ID와 월별로 그룹화합니다.
HAVING
    COUNT(*) > 0 -- 총 대여 횟수가 0보다 큰 경우에 대해서만 선택합니다.
ORDER BY 
    MONTH, CAR_ID DESC; -- 결과를 월을 기준으로 오름차순으로 정렬하고, 월이 같은 경우에는 자동차 ID를 기준으로 내림차순으로 정렬합니다.