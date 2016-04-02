#!/usr/bin/python


def main():
 x = 2 * 2 * 2 * 2 * 3 * 3 * 5 * 7 * 11 * 13 * 17 * 19
 for d in xrange(1,21):
  print '%d \ %d = %d' % (x,d,(x % d))


if __name__ == '__main__':
 main()
