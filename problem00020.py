#!/usr/bin/python


def factorial(n):
 if n == 1:
  return 1
 else:
  return n * factorial(n-1)


def main():
 print sum(map(int, str(factorial(100))))


if __name__ == '__main__':
 main()
