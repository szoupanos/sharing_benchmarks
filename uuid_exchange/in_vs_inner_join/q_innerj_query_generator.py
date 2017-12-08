#!/usr/bin/env python

import sys

print sys.argv

command = list()
command.append("\\timing on\n")
command.append("SELECT db_dbnode_1.uuid AS db_dbnode_1_uuid ")
command.append("FROM db_dbnode AS db_dbnode_1 ")
command.append("INNER JOIN ( VALUES ")

limit = int(sys.argv[2])
counter = 0
with open(sys.argv[1]) as f:
	for line in f:
		if counter == limit:
			break
	
		command.append('(\'' + line.rstrip())
		counter += 1
	
		# For the last comma
		if counter == limit:
			command.append('\')')
		else:
			command.append('\'), ')
    

command.append(") vals(v) ON (db_dbnode_1.uuid = v);")
print ''.join(command)
