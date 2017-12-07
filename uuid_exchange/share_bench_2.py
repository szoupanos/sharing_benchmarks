# -*- coding: utf-8 -*-
###########################################################################
# Copyright (c), The AiiDA team. All rights reserved.                     #
# This file is part of the AiiDA code.                                    #
#                                                                         #
# The code is hosted on GitHub at https://github.com/aiidateam/aiida_core #
# For further information on the license, see the LICENSE.txt file        #
# For further information please visit http://www.aiida.net               #
###########################################################################

from aiida.orm.querybuilder import QueryBuilder
from aiida.orm.node import Node
from sqlalchemy import event
from sqlalchemy.engine import Engine
import time

# This is the basic approach for calculating the UUIDs of the nodes to be
# sent to the receiver side.
#
# Let TS be the set of UUIDs sent by the sender and DB the set of UUIDs that
# are at the receiver side.
#
# The set calculated by SQLA is the A = DB ∩ TS
# At Python level we calculate the C = TS - A

@event.listens_for(Engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement,
                        parameters, context, executemany):
    conn.info.setdefault('query_start_time', []).append(time.time())
    # print("Start Query: %s", statement)
    print("Start Query")


@event.listens_for(Engine, "after_cursor_execute")
def after_cursor_execute(conn, cursor, statement,
                        parameters, context, executemany):
    total = time.time() - conn.info['query_start_time'].pop(-1)
    print("Query Complete!")
    print("==> Query Time (secs): {}".format(total))


# Repeat the following experiment for various UUID sizes
for lim in [100, 1000, 10000, 100000, 1000000, None]:
# for lim in [100, 1000, 10000]:
    print "<================== Round with limit", lim, "==================>"
    # Get some UUIDs -  This represents the set  of nodes that we
    # plan to send to the receiver
    start_q1 = time.time()
    qb = QueryBuilder(limit=lim)
    qb.append(Node, project=['uuid'])
    print "Got", qb.count(), "results"
    res = [_[0] for _ in qb.all()]
    end_q1 = time.time()
    print "==> Elapsed time for export query (secs)", end_q1 - start_q1

    # Store the UUIds in a file (emulate that they were send over the network
    print "Storing UUIDs to the file"
    start_s1 = time.time()
    count_s1 = 0
    with open('tmp_uuid_file.txt', 'wb') as output_file:
        for r in res:
            output_file.write(str(r)+"\n")
            count_s1 += 1
    end_s1 = time.time()
    print "Finished writing to file"
    print "Stored", count_s1, "number of lines"
    print "==> Elapsed time for writing to file (secs)", end_s1 - start_s1

    # Retrieve the UUIDs from the file
    print "Reading UUIDs from file"
    start_s2 = time.time()
    ts = list()
    count_s2 = 0
    with open('tmp_uuid_file.txt', 'rb') as input_file:
        for line in input_file:
            # obtained_uuids.append(UUID(line[:-1]))
            ts.append(line[:-1])
            count_s2 += 1
    end_s2 = time.time()
    print "Read", count_s2, "number of lines"
    print "==> Elapsed time for reading from file (secs)", end_s2 - start_s2

    # Check which the UUIDs exist in the database and get the ones that
    start_q2 = time.time()
    qb = QueryBuilder()
    qb.append(Node, filters={'uuid': {'in': ts}}, project=['uuid'])
    a = [str(_[0]) for _ in qb.all()]
    end_q2 = time.time()

    print "Found ", len(a), " of the given UUIDs in the database"
    print "==> Elapsed time for import check query (secs)", end_q2 - start_q2

    # print "obtained_uuids " + str(obtained_uuids)
    # print "existing_uuids " + str(existing_uuids)

    intersect  = list(set(ts) - set(a))
    print "Not found UUIDs :" + str(len(intersect))


