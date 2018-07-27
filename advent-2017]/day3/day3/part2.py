from __future__ import division
import math


with open('part2.txt') as f:
    count_false = 0
    count_line = 0
    orderd_word_list = []
    polyShape_sorted = []
    for line in f:
        polyShape = []
        line_string = line
        if line:            # lines (ie skip them)
            line=line.split()
            for i in line:
                if i != '\n' :
                    polyShape.append(i)

        #print "first string " + str(polyShape)
        for word in polyShape:
            polyShape_sorted.append(str(''.join(sorted(word))))

        duplicates = [x for x in polyShape_sorted if polyShape_sorted.count(x) >= 2]
        if  duplicates:
            count_false += 1
            print "Incorrect string " + str(polyShape_sorted)
        #print "For Line " + str(line_string[0:len(line_string)-1]) +   " the result is " +  str(count_false)
        duplicates = []
        count_line +=1
        polyShape_sorted=[]



    print "Total number of incorrect passphrases " + str(count_line - count_false)
#print(sum(len(l.split(" "))==len(set("".join(sorted(s))for s in l.split(" ")))for l in map(str.strip, __import__("sys").stdin.readlines())))
