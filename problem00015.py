#!/usr/bin/python


cache = dict()


def compute(d, r):
 key = str(d) + "," + str(r)
 if r > d: #no point storing the same value for 3,5 and 5,3
  key = str(r) + "," + str(d)
 if d == 0 or r == 0:
  return 1
 else:
  if key in cache:
   return cache[key]
  else:
   temp = compute(d-1, r) + compute(d, r-1)
   cache[key] = temp
   return temp


def main():
 print compute(20, 20)


if __name__ == '__main__':
 main()
