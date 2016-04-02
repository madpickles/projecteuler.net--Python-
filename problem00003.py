#!/usr/bin/python


def largestPrimeFactor(num):
 factor = 3
 while factor <= num:
  if num % factor == 0:
   num /= factor
  else:
   factor += 2
 return factor


def main():
 print largestPrimeFactor(600851475143)


if __name__ == '__main__':
 main()
