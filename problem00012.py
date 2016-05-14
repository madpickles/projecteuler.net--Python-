#!/usr/bin/python

import eulerLib


def main():
 triangle_numbers = eulerLib.triangleNumber()
 while True:
  num = triangle_numbers.next()
  prime_factorization = eulerLib.primeFactorization(num)
  divisors = eulerLib.divisorFunction(prime_factorization)
  if divisors > 500:
   print num, divisors
   break 


if __name__ == '__main__':
 main()
