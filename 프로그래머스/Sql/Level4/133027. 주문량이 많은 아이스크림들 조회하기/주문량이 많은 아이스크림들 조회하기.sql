-- FIRST_HALF 테이블과 JULY 테이블을 조인하여 상반기 아이스크림 총 주문량과 7월 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회합니다.
SELECT 
    F.FLAVOR -- 아이스크림 맛을 선택합니다.
FROM 
    FIRST_HALF AS F -- 상반기 주문 정보를 담은 테이블을 F로 지정합니다.
JOIN 
    JULY AS J ON F.FLAVOR = J.FLAVOR -- 7월 주문 정보를 담은 테이블과 조인합니다.
GROUP BY 
    F.FLAVOR -- 아이스크림 맛으로 그룹화합니다.
ORDER BY 
    (SUM(J.TOTAL_ORDER) + SUM(F.TOTAL_ORDER)) DESC -- 7월 아이스크림 총 주문량과 상반기 아이스크림 총 주문량을 더한 값으로 내림차순으로 정렬합니다.
LIMIT 3; -- 상위 3개의 맛만 선택합니다.