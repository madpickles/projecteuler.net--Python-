#!/usr/bin/python


def fibGenerator(maxFib):
    fib0 = 0
    fib1 = 1
    while fib1 < maxFib:
        yield fib1
        fibNext = fib0 + fib1
        fib0 = fib1
        fib1 = fibNext


def sumEvenFibs():
    fib = fibGenerator(4000000)
    return sum(filter((lambda x: x & 1 == 0),fib))


def evenFibGenerator(maxFib):
    fib0 = 1
    fib1 = 2
    while fib1 < maxFib:
        yield fib1
        temp = fib0 + (2 * fib1)
        fib1 = (2 * fib0) + (3 * fib1)
        fib0 = temp


def sumFibs():
    fib = evenFibGenerator(4000000)
    return sum([f for f in fib])


def main():
    print sumEvenFibs(), sumFibs()


if __name__ == '__main__':
  main()
