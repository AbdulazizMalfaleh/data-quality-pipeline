-- FULL LOAD
SELECT * FROM source_table;

-- CDC LOAD
SELECT *
FROM source_table
WHERE updated_at > %s;
