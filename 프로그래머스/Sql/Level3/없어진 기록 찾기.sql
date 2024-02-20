SELECT AO.ANIMAL_ID, AO.NAME FROM ANIMAL_OUTS AS AO
LEFT OUTER JOIN ANIMAL_INS AS AI ON 
AI.ANIMAL_ID = AO.ANIMAL_ID # 왼쪽 ANIMAL_OUTS, 오른쪽 ANIMAL_INS
# LEFT OUTER JOIN은 이처럼 JOIN 문을 수행할 때, 왼쪽에 있는 데이터는 무조건 가져오며, 오른쪽에 오는 테이블과 JOIN을 수행하여 조건에 맞는 데이터가 없을 시 null 로 표시하게 됩니다.
WHERE AI.ANIMAL_ID IS NULL
# ANIMAL_ID가 같은 값이 ANIMAL_INS 테이블에 존재하지 않는다면, NULL 값으로 연결될 것입니다.
# 이를 통해, ANIMAL_OUTS 에는 있지만 ANIMAL_INS에는 없는 ANIMAL_ID 의 값을 조회할 수 있게 됩니다.
ORDER BY AO.ANIMAL_ID;