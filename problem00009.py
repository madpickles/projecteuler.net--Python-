#!/usr/bin/python


def findPythagoreanTriplet(abcSum):
 for c in xrange(abcSum / 3 + 2, abcSum / 2):
  aPlusB = abcSum - c
  for b in xrange(aPlusB / 2 + 1, min(c, aPlusB)):
   a = aPlusB - b
   if a**2 + b**2 == c**2:
    return a * b * c


def main():
 print findPythagoreanTriplet(1000)


if __name__ == '__main__':
 main()
