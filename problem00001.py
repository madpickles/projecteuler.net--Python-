#!/usr/bin/python


def sum_multiples_of_3_and_5_v1():
    total = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total


def sum_multiples_of_3_and_5_v2():
    return sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])


def sum_multiples_of_3_and_5_v3():
    return (
        999 * ((999 / 3) + 1) +  # multiples of 3
        995 * ((995 / 5) + 1) -  # multiples of 5
        990 * ((990 / 15) + 1)   # multiples of 3 * 5
        ) / 2                    # for sum of number sequence


def main():
    print (sum_multiples_of_3_and_5_v1(), sum_multiples_of_3_and_5_v2(),
           sum_multiples_of_3_and_5_v3())


if __name__ == '__main__':
    main()
