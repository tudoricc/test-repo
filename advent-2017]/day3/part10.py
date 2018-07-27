from __future__ import division
import math

with open('part1.txt') as f:
    count_false = 0
    count_line = 0
    for line in f:
        polyShape = []
        line_string = line
        if line:            # lines (ie skip them)
            line=line.split()
            for i in line:
                if i != '\n' :
                    polyShape.append(i)

        duplicates = [x for x in polyShape if polyShape.count(x) >= 2]
        if not duplicates :
            count_false += 1
        #print "For Line " + str(line_string[0:len(line_string)-1]) +   " the result is " +  str(count_false)

        count_line +=1
    print "Total number of correct passphrases " + str(count_false)
