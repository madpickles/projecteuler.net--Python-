#!/usr/bin/python

import sys


def readRowsOfNumbersFile(f):
 g = []
 fh = open(f, "r")
 while True:
  temp = fh.readline()
  if not temp:
   break 
  g.append(map(int,temp.split()))
 fh.close()
 return g


def main(argv):
 g = readRowsOfNumbersFile(argv[1])
 g = g[::-1]
 sums = g[0]
 for r in xrange(1,len(g)):
  prevSums = sums
  row = g[r] 
  for i in xrange(len(row)):
   sums[i] = max(prevSums[i] + row[i],prevSums[i+1] + row[i])
 print sums[0]


if __name__ == '__main__':
 main(sys.argv)
