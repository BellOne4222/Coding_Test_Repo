-- CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블과 CAR_RENTAL_COMPANY_DISCOUNT_PLAN 테이블에서
-- 자동차 종류가 '트럭'인 자동차의 대여 기록에 대해서 대여 기록 별로 대여 금액을 구합니다.
SELECT 
    HISTORY_ID, -- 대여 기록 ID를 선택합니다.
    ROUND(DAILY_FEE * (DATEDIFF(RH.END_DATE, RH.START_DATE) + 1) -- 대여 기간에 따른 요금을 계산합니다.
    * (CASE 
        WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 7 THEN 1 -- 대여 기간이 7일 미만인 경우 할인이 적용되지 않습니다.
        WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 30 THEN 0.95 -- 대여 기간이 7일 이상, 30일 미만인 경우 5% 할인이 적용됩니다.
        WHEN DATEDIFF(END_DATE, START_DATE) + 1 < 90 THEN 0.92 -- 대여 기간이 30일 이상, 90일 미만인 경우 8% 할인이 적용됩니다.
        ELSE 0.85 -- 대여 기간이 90일 이상인 경우 15% 할인이 적용됩니다.
    END)) AS "FEE" -- 총 대여 금액을 계산합니다.
FROM 
    CAR_RENTAL_COMPANY_CAR AS C 
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS RH ON C.CAR_ID = RH.CAR_ID -- 자동차 대여 기록과 자동차 정보를 조인합니다.
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS DP ON C.CAR_TYPE = DP.CAR_TYPE -- 자동차 종류별 할인 정책 정보를 조인합니다.
WHERE 
    C.CAR_TYPE = '트럭' -- 자동차 종류가 '트럭'인 대여 기록을 선택합니다.
GROUP BY 
    HISTORY_ID -- 대여 기록 ID로 그룹화합니다.
ORDER BY 
    FEE DESC, -- 대여 금액을 기준으로 내림차순으로 정렬합니다.
    HISTORY_ID DESC; -- 대여 금액이 같은 경우 대여 기록 ID를 기준으로 내림차순으로 정렬합니다.