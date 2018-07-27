from __future__ import division
import math

import json

import pprint

with open('part2.txt') as f:

    for line in f:
        captcha_list = []
        if line:            # lines (ie skip them)
            #print line
            for i in range(0,len(line)):
                if line[i] != '\n':
                    #print line[i]
                    captcha_list.append(int(line[i]))
        #print len(captcha_list)
        how_many_steps_to_jump_to = int(len(captcha_list) / 2)
        # 0 1 2 3
        # len = 4
        # step = 2
        sum_of_matching = 0
        for index in range(0,int(len(captcha_list) / 2 )):
            if captcha_list[index] == captcha_list[index+how_many_steps_to_jump_to]:
                sum_of_matching += 2*captcha_list[index]

#        print "For line  " + str(captcha_list) + " We have the sum of " + str(sum_of_matching)
        print str(sum_of_matching)
