SELECT (CASE WHEN c.reltuples < 0 THEN NULL       -- never vacuumed
             WHEN c.relpages = 0 THEN float8 '0'  -- empty table
             ELSE c.reltuples / c.relpages END
     * (pg_catalog.pg_relation_size(c.oid)
      / pg_catalog.current_setting('block_size')::int)
       )::bigint
FROM   pg_catalog.pg_class c
WHERE  c.oid = 'myschema.mytable'::regclass;      -- schema-qualified table here
