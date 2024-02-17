# 서브 쿼리

# SELECT ITEM_ID, ITEM_NAME, RARITY FROM ITEM_INFO
# WHERE ITEM_ID IN(SELECT ITEM_ID FROM ITEM_TREE WHERE PARENT_ITEM_ID IN (SELECT ITEM_ID FROM ITEM_INFO WHERE RARITY = 'RARE')) # 1,2,3,4
# ORDER BY ITEM_ID DESC;

# LEFT JOIN

SELECT ITEM_ID, ITEM_NAME, RARITY FROM ITEM_INFO
WHERE ITEM_ID IN(
    SELECT IT.ITEM_ID FROM ITEM_INFO AS II
    LEFT JOIN ITEM_TREE AS IT ON II.ITEM_ID = IT.PARENT_ITEM_ID
    WHERE II.RARITY = 'RARE' AND IT.ITEM_ID IS NOT NULL # ROOT 아이템 제외
    )
ORDER BY ITEM_ID DESC;
