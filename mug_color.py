#!/usr/bin/python
#Problem        : Mug Color
#Language       : Python
#by Joe Velardo

from __future__ import print_function
import sys

colors = ["White", "Black", "Blue", "Red", "Yellow"]
not_these = []
count = 0

num = raw_input()
num = int(num)

while count < num:
      color_entry = raw_input()
      not_these.append(str(color_entry))
      count += 1

for x in not_these:
    for y in colors:
        if x == y:
           colors.remove(y)

print("The mug is "+ colors[0])
