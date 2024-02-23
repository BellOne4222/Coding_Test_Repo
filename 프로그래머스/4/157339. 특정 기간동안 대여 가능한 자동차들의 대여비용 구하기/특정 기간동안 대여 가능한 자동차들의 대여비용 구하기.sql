-- CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서
-- 자동차 종류가 '세단' 또는 'SUV' 인 자동차 중 2022년 11월 1일부터 2022년 11월 30일까지 대여 가능하고
-- 30일간의 대여 금액이 50만원 이상 200만원 미만인 자동차에 대해서 자동차 ID, 자동차 종류, 대여 금액 리스트를 출력합니다.
SELECT 
    C.CAR_ID, -- 자동차 ID를 선택합니다.
    C.CAR_TYPE, -- 자동차 종류를 선택합니다.
    ROUND(C.DAILY_FEE * 30 * (100 - P.DISCOUNT_RATE) / 100) AS FEE -- 대여 금액을 계산합니다.
FROM 
    CAR_RENTAL_COMPANY_CAR AS C -- 자동차 정보를 담은 테이블을 C로 지정합니다.
JOIN 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H ON C.CAR_ID = H.CAR_ID -- 자동차 대여 기록 정보를 담은 테이블과 조인합니다.
JOIN 
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P ON C.CAR_TYPE = P.CAR_TYPE -- 자동차 종류별 할인 정책 정보를 담은 테이블과 조인합니다.
WHERE 
    C.CAR_ID NOT IN (
        SELECT 
            CAR_ID
        FROM 
            CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE 
            END_DATE > '2022-11-01' AND START_DATE < '2022-12-01' -- 2022년 11월 1일부터 2022년 11월 30일까지 대여 중인 자동차를 제외합니다.
    ) 
    AND P.DURATION_TYPE = '30일 이상' -- 대여 기간이 30일 이상인 경우를 선택합니다.
GROUP BY 
    C.CAR_ID -- 자동차 ID로 그룹화합니다.
HAVING 
    C.CAR_TYPE IN ('세단', 'SUV') AND (FEE >= 500000 AND FEE < 2000000) -- 자동차 종류가 '세단' 또는 'SUV'이고 대여 금액이 50만원 이상 200만원 미만인 경우를 선택합니다.
ORDER BY 
    FEE DESC, -- 대여 금액을 기준으로 내림차순으로 정렬합니다.
    CAR_TYPE, -- 자동차 종류를 기준으로 오름차순으로 정렬합니다.
    CAR_ID DESC; -- 대여 금액이 같은 경우 자동차 ID를 기준으로 내림차순으로 정렬합니다.
