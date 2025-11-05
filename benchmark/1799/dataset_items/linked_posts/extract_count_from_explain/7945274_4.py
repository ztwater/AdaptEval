SELECT (reltuples / relpages * (pg_relation_size(oid) / 8192))::bigint
FROM   pg_class
WHERE  oid = 'mytable'::regclass;  -- your table here
