# PostgreSQL experiments using IN and INNER JOIN
References:  
- https://dba.stackexchange.com/questions/91247/optimizing-a-postgres-query-with-a-large-in
- https://stackoverflow.com/questions/24647503/performance-issue-in-update-query

All experiments were run after cleaning the cache.  
sync; /etc/init.d/postgresql stop; echo 1 > /proc/sys/vm/drop_caches; /etc/init.d/postgresql start  

Sample of how each of the queries was run:  
psql -p 5433 -d aiidadb_mounet_new_sqla -a -f "/tmp/q_innerj_100.sql" -o /tmp/q_out.txt

## Results
- [IN query with 100 entries, q_in_100.sql](./q_in_100.sql): 705.672 ms
- [INNER JOIN query with 100 entries, q_innerj_100.sql](./q_innerj_100.sql): 547.907 ms
- [IN query with 1000 entries, q_in_1000.sql](./q_in_1000.sql): 912.600 ms
- [INNER JOIN query with 1000 entries, q_innerj_1000.sql](./q_innerj_1000.sql): 806.591 ms


