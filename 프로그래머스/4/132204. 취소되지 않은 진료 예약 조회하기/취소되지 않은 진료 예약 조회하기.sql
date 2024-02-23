-- APPOINTMENT, PATIENT, DOCTOR 테이블에서 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회합니다.
SELECT 
    A.APNT_NO, -- 진료예약번호를 선택합니다.
    P.PT_NAME, -- 환자이름을 선택합니다.
    A.PT_NO, -- 환자번호를 선택합니다.
    A.MCDP_CD, -- 진료과코드를 선택합니다.
    D.DR_NAME, -- 의사이름을 선택합니다.
    A.APNT_YMD -- 진료예약일시를 선택합니다.
FROM 
    APPOINTMENT AS A -- 진료 예약 정보를 나타내는 테이블을 A로 지정합니다.
JOIN 
    PATIENT AS P ON A.PT_NO = P.PT_NO -- 환자 정보를 나타내는 테이블과 조인합니다.
JOIN 
    DOCTOR AS D ON A.MDDR_ID = D.DR_ID -- 의사 정보를 나타내는 테이블과 조인합니다.
WHERE 
    A.APNT_YMD LIKE '2022-04-13%' -- 진료 예약일시가 2022년 4월 13일인 경우를 선택합니다.
    AND A.APNT_CNCL_YN = 'N' -- 진료 예약이 취소되지 않은 경우를 선택합니다.
    AND A.MCDP_CD = 'CS' -- 진료과코드가 'CS'인 경우를 선택합니다.
ORDER BY 
    APNT_YMD ASC; -- 진료예약일시를 기준으로 오름차순으로 결과를 정렬합니다.