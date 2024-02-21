# 조인 사용
select ugb.writer_id user_id, 
ugu.nickname nickname, 
concat(ugu.city, ' ', ugu.street_address1, ' ', ugu.street_address2) AS 전체주소, 
concat(left(ugu.tlno, 3), '-', mid(ugu.tlno, 4, 4), '-', right(ugu.tlno, 4)) AS 전화번호
from used_goods_board ugb
join used_goods_user ugu
on ugb.writer_id = ugu.user_id
group by ugb.writer_id
having count(*) >= 3
order by ugu.user_id desc

# 서브 쿼리 사용
SELECT  USER_ID
        , NICKNAME
        , CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS '전체주소'
        , CONCAT(SUBSTR(TLNO, 1, 3), '-', SUBSTR(TLNO, 4, 4), '-', SUBSTR(TLNO, 8)) AS '전화번호'
FROM    USED_GOODS_USER 
WHERE   USER_ID IN (
                     SELECT  WRITER_ID
                     FROM    USED_GOODS_BOARD
                     GROUP BY WRITER_ID
                     HAVING  COUNT(*) >= 3
                 )
 ORDER BY  USER_ID DESC;