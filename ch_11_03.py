import re
hand = open('lorem.txt')
numlist = list()

for line in hand:
    line = line.rstrip()
    stuff = re.findall('sed', line)
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)

print('Maximum: ', numlist)