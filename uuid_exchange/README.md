# UUID exchange benchmarks

Let’s call:  
DB the set of UUIDs at the receiver side  
TS the set of UUIDs sent by the sender  
B = DB - TS  
A = DB - B (which is also DB ∩ TS)  
C = TS - A (which is also TS - DB)  

I performed most of the experiments with a subset of the database of Nicolas Mounet with 1.462.993 nodes  
The large Db which is mentioned below is a 7.318.371 node database obtained by Nicolas Mounet.

The bench2_1 (my initial approach):  
Calculates at the SQLA level the A = DB ∩ TS and calculates at the python level the C = TS - A  
[Sharing bench 2 - Script](./share_bench_2_1.py)  
[Sharing bench 2 - Results with small DB](./sharing_bench21_res1_smalldb.txt)  
[Sharing bench 2 - Results with small DB - Clean cache](./sharing_bench21_res2_smalldb_empty_cache.txt)  
[Sharing bench 2 - Results with small DB - PC restart](./sharing_bench21_res3_smalldb_restart.txt)  


The bench3:
Calculates at the SQLA level the B = DB - TS
and calculates at the python level the A = DB - B and finally the C = TS - A
It is a bit schizophrenic this approach but it is the first idea that came to my mind that uses the B = DB - TS that you proposed.
The calculation times are also schizophrenic…. :)  
[Sharing bench 3 - Script](./share_bench_3.py)  
[Sharing bench 3 - Results with small DB](./sharing_bench3_res1_smalldb.txt)

The bench4:
In this approach we pass to PostgreSQL the calculation of the final set C, where C = TS - DB  
[Sharing bench 4 - Script](./share_bench_4.py)  
[Sharing bench 4 - Results with small DB](./sharing_bench4_res1_smalldb.txt)

The bench5:
In this approach we get from SQLA the DB set and we calculate the C at the Python level, where C = TS - DB  
[Sharing bench 5 - Script](./share_bench_5.py)  
[Sharing bench 5 - Results with small DB](./sharing_bench5_res1_smalldb.txt)

The bench 6:
In this approach we get from SQLA the DB set and we calculate the C at the Python level, where C = TS - DB
The difference with 5 is that we bypass the QueryBuilder for the receiver check and we use the SQLA API  
[Sharing bench 6 - Script](./share_bench_6.py)  
[Sharing bench 6 - Results with small DB](./sharing_bench6_res1_smalldb.txt)  
[Sharing bench 6 - Results with small DB - Clean cache](./sharing_bench6_res2_smalldb_empty_cache.txt)  
[Sharing bench 6 - Results with small DB - PC restart](./sharing_bench6_res3_smalldb_restart.txt)  
[Sharing bench 6 - Results with lange DB](./sharing_bench6_res1_mounetdb.txt)  

From a first look, the most promising approaches are 2 & 6.