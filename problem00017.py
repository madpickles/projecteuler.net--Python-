#!/usr/bin/python


def main():
 oneToNine = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
 tenToNineteen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen", "nineteen"]
 ties = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

 oneToNinetynineCount = sum([len(x) for x in oneToNine])
 oneToNinetynineCount += sum([len(x) for x in tenToNineteen])
 oneToNinetynineCount += sum([len(x) for x in ties])
 oneToNinetynineCount += sum([len(x)+len(y) for x in ties for y in oneToNine])

 total = oneToNinetynineCount

 # 100 to 999
 for x in oneToNine:
  xHundredCount = len(x) + 7 # hundred = 7 chars
  total += xHundredCount + (xHundredCount + 3) * 99 + oneToNinetynineCount # and = 3 chars

 print total + len("onethousand")


if __name__ == '__main__':
 main()
