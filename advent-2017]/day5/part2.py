from __future__ import division
import math



#(0) 3  0  1  -3
#29629538
with open('part2.txt') as f:
    instructions = []
    for line in f:

        if line:            # lines (ie skip them)
            instructions.append(int(line))

    #print instructions
    #you should have the whole string
    current_pos = 0
    steps_to_advance = 0
    i = 0
# (1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all). Fortunately, the instruction is then incremented to 1.
#  2 (3) 0  1  -3  - step forward because of the instruction we just modified. The first instruction is incremented again, now to 2.
# 2 (2) 0 1 -2
# 2 2 (2) 1 -2
# 2 2 3 1 (-2)
# 2 2 (3) 1 (-1)
# 2 2 2 1
    print len(instructions)
    while (i != len(instructions) and i >= 0):
        #print "I value is " + str(i)
        #old_value = instructions[i]
        if instructions[i] == 0:
            #print "Also here"
            instructions[i] = instructions[i] + 2
            i += 1
            steps_to_advance += 2
        else:

            if instructions[i]  >= 3 :
                old_value = instructions[i]
                instructions[i] = instructions[i] - 1
                i += instructions[i] + 1 
                steps_to_advance += 1
            else :
                #print "Comes here"
                instructions[i] = instructions[i] + 1
                i += instructions[i] - 1
                steps_to_advance += 1






    print "Number of steps for exiting " + str(steps_to_advance)
