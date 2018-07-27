from __future__ import division
import math



#(0) 3  0  1  -3
#29629538
with open('part2.txt') as f:
    instructions = []
    for line in f:
#        print line

        if line:            # lines (ie skip them)
            line_string =  line.split("\t")
            for number in line_string:
                instructions.append(int(number))
#    print instructions


    old_configuration = {}
    old_configuration_index = 0

    old_configuration[old_configuration_index] = instructions[:]

#0 2 7 0
#2 4 1 2
#
    #print old_configuration
    found_old_occurence = False
    print "Length is " + str(len(instructions))
    while found_old_occurence != True :
        max_index = instructions.index(max(instructions))
        max_value = max(instructions)
        i = max_index
        instructions[max_index] = 0
        while max_value != 0 :
                i = (i+1) % len(instructions)
                instructions[i] = instructions[i] + 1
                max_value = max_value - 1

        #print instructions
        for key in old_configuration.keys():

            if instructions == old_configuration[key]:
                # print str(old_configuration) + " Are the old values"
                # print str(instructions) + " Are the current values"
                found_old_occurence = True

        old_configuration_index += 1
        old_configuration[old_configuration_index] = instructions[:]
    for pos, list_of_values in old_configuration.iteritems():
        if list_of_values == instructions:
            print str(len(old_configuration.keys()) - pos)
    print "Number of actual steps " + str(len(old_configuration.keys()) - old_configuration_index)
