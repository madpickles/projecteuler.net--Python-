#!/usr/bin/python

import operator


def triangleNumber():
 num = 1
 add = 2
 while True:
  yield num
  num += add
  add += 1


def primeFactorization(num):
 factors = []
 while 2 <= num:
  if num & 1:
   break
  else:
   num = num >> 1
   factors.append(2)
 factor = 3
 while factor <= num:
  if num % factor == 0:
   num /= factor
   factors.append(factor)
  else:
   factor += 2
 return factors


def uniqueCounts(l):
 counts = []
 count = 0
 previous = None
 for x in l:
  if x == previous:
   count += 1
  else:
   counts.append(count+1)
   count = 1
   previous = x
 counts.append(count+1)
 return counts


def divisorFunction(factors):
 return reduce(operator.mul, uniqueCounts(factors))
