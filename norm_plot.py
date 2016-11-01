from __future__ import print_function

import sys
import os

largv = len(sys.argv)

if largv < 2:
	sys.exit('Please supply plot files to normalize')

largv -= 1

print("Normalizing files:", largv)
avg_file = open('average.plot', 'r')

for idx in range(largv):
	avg_file.seek(0)
	fname = sys.argv[idx + 1]
	file = open(fname, 'r')
	n_fname = os.path.dirname(fname) + "/New Plots/" + os.path.basename(fname)
	o_file = open(n_fname, 'w')
	for line in file:
		avg_line = avg_file.readline()
		sval = line.split(' ')
		sval_avg = avg_line.split(' ')
		hz = int(int(sval[0]) / 10) * 10
		db = float(sval[1])
		a_db = float(sval_avg[1])
		db = db - a_db
		o_file.write(repr(hz) + " " + repr(db) + "\n")
	file.close()
	o_file.close()

avg_file.close()
