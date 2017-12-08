# PostgreSQL experiments using IN and INNER JOIN
References:  
- https://dba.stackexchange.com/questions/91247/optimizing-a-postgres-query-with-a-large-in
- https://stackoverflow.com/questions/24647503/performance-issue-in-update-query

All experiments were run after cleaning the cache.  
- sync; /etc/init.d/postgresql stop; echo 1 > /proc/sys/vm/drop_caches; /etc/init.d/postgresql start  

Sample of how each of the queries was run:  
- psql -p 5433 -d aiidadb_mounet_new_sqla -a -f "/home/szoupanos/aiida/sharing_benchmarks/uuid_exchange/in_vs_inner_join/q_innerj_1000000.sql" -o /tmp/lala.txt > /tmp/res.txt
- tail -n 1  /tmp/res.txt

## Results
- [IN query with 100 entries, q_in_100.sql](./q_in_100.sql): 727.184 ms
- [INNER JOIN query with 100 entries, q_innerj_100.sql](./q_innerj_100.sql): 681.677 ms
- [IN query with 1.000 entries, q_in_1000.sql](./q_in_1000.sql): 644.894 ms
- [INNER JOIN query with 1000 entries, q_innerj_1000.sql](./q_innerj_1000.sql): 650.943 ms
- [IN query with 10.000 entries, q_in_10000.sql](./q_in_10000.sql): 665.496 ms
- [INNER JOIN query with 10.000 entries, q_innerj_10000.sql](./q_innerj_10000.sql): 771.563 ms
- [IN query with 100.000 entries, q_in_100000.sql](./q_in_100000.sql): 1491.073 ms
- [INNER JOIN query with 100.000 entries, q_innerj_100000.sql](./q_innerj_100000.sql): 1407.105 ms
- [IN query with 1.000.000 entries, q_in_1000000.sql](./q_in_1000000.sql): 7935.396 ms
- [INNER JOIN query with 1.000.000 entries, q_innerj_1000000.sql](./q_innerj_1000000.sql): 8701.347 ms
