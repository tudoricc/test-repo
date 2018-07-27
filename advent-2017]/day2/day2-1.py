from __future__ import division
import math

with open('data.txt') as f:
    sum_of_lines = 0
    for line in f:
#      print "----------"
      polyShape = []
      print
      if line:            # lines (ie skip them)
        line=line.split()
        for i in line:
            if i != '\n' :
                polyShape.append(int(i))

        sum_of_differences=0
        origina_length=len(polyShape)
        max_value = max(polyShape)
        min_value = min(polyShape)

        diff = 0
        diff = max_value - min_value
        sum_of_lines += diff


    print "Sum is " + str(sum_of_lines)
