#!/usr/bin/python


cache = dict()
cache[1] = 1
maxCount = [1,1]


def find(n,m):
 newN = 0
 if n in cache:
  return cache[n]
 elif n % 2 == 0:
  newN = n / 2
 else:
  newN = 3 * n +1
 temp = 1 + find(newN,m)
 cache[n] = temp 
 if temp > m[1] and n < 1000000:
  m[0] = n
  m[1] = temp
 return cache[n]


def main():
 for i in xrange(2,1000000):
  find(i, maxCount)
 print maxCount


if __name__ == '__main__':
 main()

