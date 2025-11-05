SELECT reltuples::bigint AS estimate
FROM   pg_class
WHERE  oid = 'myschema.mytable'::regclass;
