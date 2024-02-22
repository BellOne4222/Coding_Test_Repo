-- 변수 @HOUR을 -1로 초기화
SET @HOUR = -1;

-- 0부터 23까지의 시간(HOUR)에 따른 각 시간대별 동물 이탈 횟수를 조회하는 쿼리
SELECT 
    -- @HOUR 값을 1씩 증가시키면서 시간을 나타내는 HOUR 컬럼 생성
    (@HOUR := @HOUR + 1) AS HOUR,
    -- 서브쿼리: ANIMAL_OUTS 테이블에서 DATETIME에서 추출한 시간이 @HOUR과 일치하는 레코드의 개수를 조회하여 COUNT 컬럼 생성
    (SELECT COUNT(HOUR(DATETIME)) 
    FROM ANIMAL_OUTS 
    WHERE HOUR(DATETIME) = @HOUR) AS COUNT 
-- ANIMAL_OUTS 테이블을 대상으로 함
FROM ANIMAL_OUTS
-- @HOUR이 23보다 작을 때까지만 조회하여 시간 범위를 0부터 22까지로 제한
WHERE @HOUR < 23;