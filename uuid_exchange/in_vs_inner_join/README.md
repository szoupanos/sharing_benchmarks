# PostgreSQL experiments using IN and INNER JOIN
References:  
- https://dba.stackexchange.com/questions/91247/optimizing-a-postgres-query-with-a-large-in
- https://stackoverflow.com/questions/24647503/performance-issue-in-update-query

All experiments were run after cleaning the cache.  
sync; /etc/init.d/postgresql stop; echo 1 > /proc/sys/vm/drop_caches; /etc/init.d/postgresql start  

Sample of how each of the queries was run:  
psql -p 5433 -d aiidadb_mounet_new_sqla -a -f "/tmp/q_innerj_100.sql" -o /tmp/q_out.txt

## Results
