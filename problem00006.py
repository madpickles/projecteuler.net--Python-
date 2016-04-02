#!/usr/bin/python


def p6(r):
 return sum(r)** 2 - sum([x** 2 for x in r])


def main():
 print p6(range(101))


if __name__ == '__main__':
 main()
