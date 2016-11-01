from __future__ import print_function

import sys

largv = len(sys.argv)

if largv < 2:
	sys.exit('Please supply plot files to average out')

largv -= 1

avg_val = [0.0] * 22000

print("Averaging files:", largv)

for idx in range(largv):
	fname = sys.argv[idx + 1]
	file = open(fname, 'r')
	for line in file:
		sval = line.split(' ')
		hz = int(int(sval[0]) / 10) * 10
		db = float(sval[1])
		mfactor = idx / (idx + 1)
		avg_val[hz] *= mfactor
		add_val = db / (idx + 1)
		avg_val[hz] += add_val
	file.close()

avg_val = [x * largv for x in avg_val]

f = open('average.plot', 'w')
for index, item in enumerate(avg_val):
	if item > 0:
		f.write(repr(index) + " " + repr(item) + "\n")
f.close()
