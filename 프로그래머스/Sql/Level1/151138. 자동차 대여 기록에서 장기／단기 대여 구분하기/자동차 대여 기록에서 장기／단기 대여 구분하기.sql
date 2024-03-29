# 1. 2022년 9월에 속하는 대여기록만.
# 2. 대여 기간일을 빼기
# 3. 새로운 컬럼을 추가하기
# 4. 뺀 대여기간이 30일 이상일경우 '장기대여' 아닐경우 '단기대여'
# 5. 결과는 내림차순으로  

# SELECT HISTORY_ID, CAR_ID, 
#         DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE, 
#         DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE, 
#         CASE WHEN DATEDIFF(END_DATE, START_DATE) < 29 THEN '단기대여' ELSE '장기대여' END AS RENT_TYPE
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE START_DATE LIKE '2022-09-%'
# ORDER BY HISTORY_ID DESC;

SELECT HISTORY_ID, CAR_ID, 
	   DATE_FORMAT (START_DATE, "%Y-%m-%d") AS START_DATE, 
	   DATE_FORMAT (END_DATE, "%Y-%m-%d") AS END_DATE,
CASE WHEN DATEDIFF(END_DATE, START_DATE) < 29 then '단기 대여' 
            ELSE '장기 대여' 
            END AS  RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE '2022-09-%'
ORDER BY HISTORY_ID DESC;
