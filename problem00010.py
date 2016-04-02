#!/usr/bin/python


def main():
 mx = 2000000
 maxM = mx - 2
 r = range(2, mx)
 c = 1
 for n in r:
  m = n - 2
  if r[m] != 0:
   c += 1
   m += n
   while m < maxM:
    r[m] = 0
    m += n

 print sum(r)


if __name__ == '__main__':
 main()
