#!/usr/bin/python


total = 0
f = open("problem0013.txt","r")
while True:
 temp = f.readline()
 if not temp:
  break
 total += int(temp[0:11])
f.close()
print str(total)[:10]


if __name__ == '__main__':
 main()
