#!/usr/bin/python


def main():
 mx = 105000
 maxM = mx - 2
 r = range(2, mx)
 c = 1
 for n in r:
  m = n - 2
  if r[m] != 0:
   print "prime %d is %d" % (c,n)
   c += 1
   m += n
   while m < maxM:
    r[m] = 0
    m += n


if __name__ == '__main__':
 main()
