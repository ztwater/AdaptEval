SELECT (case when cnt > 500000 then 500000 else cnt end) myCnt
FROM (SELECT count(*) cnt FROM table WHERE rownum<=500001)
