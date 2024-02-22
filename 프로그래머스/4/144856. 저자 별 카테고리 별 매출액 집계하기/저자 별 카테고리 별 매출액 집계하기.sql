SELECT B.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY, SUM(S.SALES * B.PRICE) AS TOTAL_SALES FROM BOOK AS B
JOIN AUTHOR AS A ON B.AUTHOR_ID = A.AUTHOR_ID 
JOIN BOOK_SALES AS S ON B.BOOK_ID = S.BOOK_ID
WHERE S.SALES_DATE LIKE '2022-01%'
GROUP BY AUTHOR_ID, CATEGORY
ORDER BY B.AUTHOR_ID ASC, B.CATEGORY DESC;
