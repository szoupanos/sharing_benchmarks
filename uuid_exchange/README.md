# UUID exchange benchmarks

Let’s call:
DB the set of UUIDs at the receiver side
TS the set of UUIDs sent by the sender
B = DB - TS
A = DB - B (which is also DB ∩ TS)
C = TS - A (which is also TS - DB)

I performed most of the experiments with a subset of the database of Mounet with 1.462.993 nodes

The bench2_1 (my initial approach):
Calculates at the SQLA level the A = DB ∩ TS and calculates at the python level the C = TS - A
[Sharing bench 2](./share_bench_2_1.py)
https://github.com/szoupanos/sharing_benchmarks/blob/master/uuid_exchange/sharing_bench21_res1_smalldb.txt

The bench3:
Calculates at the SQLA level the B = DB - TS
and calculates at the python level the A = DB - B and finally the C = TS - A
It is a bit schizophrenic this approach but it is the first idea that came to my mind that uses the B = DB - TS that you proposed.
The calculation times are also schizophrenic…. :)
https://github.com/szoupanos/sharing_benchmarks/blob/master/uuid_exchange/share_bench_3.py
https://github.com/szoupanos/sharing_benchmarks/blob/master/uuid_exchange/sharing_bench3_res1_smalldb.txt

The bench4:
In this approach we pass to PostgreSQL the calculation of the final set C, where C = TS - DB
https://github.com/szoupanos/sharing_benchmarks/blob/master/uuid_exchange/share_bench_4.py
https://github.com/szoupanos/sharing_benchmarks/blob/master/uuid_exchange/sharing_bench4_res1_smalldb.txt

The bench5:
In this approach we get from SQLA the DB set and we calculate the C at the Python level, where C = TS - DB
https://github.com/szoupanos/sharing_benchmarks/blob/master/uuid_exchange/share_bench_5.py
https://github.com/szoupanos/sharing_benchmarks/blob/master/uuid_exchange/sharing_bench5_res1_smalldb.txt

The bench 6:
In this approach we get from SQLA the DB set and we calculate the C at the Python level, where C = TS - DB
The difference with 5 is that we bypass the QueryBuilder for the receiver check and we use the SQLA API
https://github.com/szoupanos/sharing_benchmarks/blob/master/uuid_exchange/share_bench_6.py
https://github.com/szoupanos/sharing_benchmarks/blob/master/uuid_exchange/sharing_bench6_res1_smalldb.txt
https://github.com/szoupanos/sharing_benchmarks/blob/master/uuid_exchange/sharing_bench6_res1_mounetdb.txt

From a first look, the most promising approaches are 1 & 6.