 SELECT reltuples::bigint AS EstimatedCount
    FROM   pg_class
    WHERE  oid = 'public.TableName'::regclass;
