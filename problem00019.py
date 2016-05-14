#!/usr/bin/python


def main(): 
 daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
 daysInMonthLeap = [31,29,31,30,31,30,31,31,30,31,30,31]

 # go through year 1900 to set firstDay properly for 1901
 firstDay = 1 # Monday
 for m in daysInMonth:
  firstDay += m
  firstDay = firstDay % 7

 sun1stMonths = 0 
 for y in xrange(1901,2001):
  dim = daysInMonth
  if y % 4 == 0:
   dim = daysInMonthLeap
  for m in dim:
   if firstDay % 7 == 0: # Sunday
    sun1stMonths += 1 
   firstDay += m 
   firstDay = firstDay % 7
 print sun1stMonths


if __name__ == '__main__':
 main()
