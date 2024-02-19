# 서브 쿼리

# 희귀도가 'RARE'인 아이템의 부모 아이템이 있는지 확인하기 위해 해당 부모 아이템의 아이템 ID를 선택
SELECT ITEM_ID, ITEM_NAME, RARITY FROM ITEM_INFO
WHERE ITEM_ID IN(
    # 희귀도가 'RARE'인 아이템의 아이템 ID를 선택하여 그 아이템이 부모 아이템인 아이템들을 찾음
    SELECT ITEM_ID FROM ITEM_TREE
    WHERE PARENT_ITEM_ID IN (
        # 희귀도가 'RARE'인 아이템들의 아이템 ID를 선택
        SELECT ITEM_ID FROM ITEM_INFO WHERE RARITY = 'RARE'
    )
)
ORDER BY ITEM_ID DESC;

# LEFT JOIN

# 아이템 정보 테이블에서 희귀도가 'RARE'인 아이템들의 아이템 ID를 선택
SELECT ITEM_ID, ITEM_NAME, RARITY FROM ITEM_INFO
WHERE ITEM_ID IN(
    # 아이템 정보와 아이템 트리를 조인하여 업그레이드 가능한 아이템들의 아이템 ID를 선택
    SELECT IT.ITEM_ID FROM ITEM_INFO AS II
    LEFT JOIN ITEM_TREE AS IT ON II.ITEM_ID = IT.PARENT_ITEM_ID
    WHERE II.RARITY = 'RARE' AND IT.ITEM_ID IS NOT NULL # ROOT 아이템 제외
    )
ORDER BY ITEM_ID DESC;