#!/usr/bin/python

import sys


sys.setrecursionlimit(7000)


def findLargestPalindrome():
 factorA = 999
 factorB = factorA
 maxToCheck = 100
 maxPalindrome = 0

 while factorA > maxToCheck:
  factorB = factorA
  while factorB > maxToCheck:
   temp = factorA * factorB
   if temp < maxPalindrome:
    maxToCheck = factorB
    break
   else:
    tempStr = str(temp)
    if tempStr == tempStr[::-1]:
     maxToCheck = factorB
     maxPalindrome = temp
     break
   factorB -= 1
  factorA -= 1
 return maxPalindrome


def findLargestPalindrome2(factorA, factorB, maxToCheck, maxPalindrome):
 if factorA < maxToCheck:
  return maxPalindrome
 elif factorB < maxToCheck:
  newFactor = factorA - 1
  return findLargestPalindrome2(newFactor, newFactor,  maxToCheck, maxPalindrome)
 else:
  candidate = factorA * factorB
  if candidate < maxPalindrome:
   newFactor = factorA - 1
   return findLargestPalindrome2(newFactor, newFactor, factorB, maxPalindrome)
  else:
   tempStr = str(candidate)
   if tempStr == tempStr[::-1]:
    newFactor = factorA - 1
    return findLargestPalindrome2(newFactor, newFactor, factorB, candidate)
   else:
    return findLargestPalindrome2(factorA, factorB - 1, maxToCheck, maxPalindrome)


def main():
 print (findLargestPalindrome(), findLargestPalindrome2(999, 999, 100, 0))

 
if __name__ == '__main__':
 main()
