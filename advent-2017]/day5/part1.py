from __future__ import division
import math



#(0) 3  0  1  -3

with open('part1.txt') as f:
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
#  2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
#  2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
#  2  5  0  1  -2

    while i < len(instructions):
        #print "I value is " + str(i)
        old_value = instructions[i]
        if instructions[i] == 0:
            instructions[i] = instructions[i] + 2
            i += 1
            steps_to_advance += 2
        else:
            instructions[i] = instructions[i] + 1
            i += instructions[i] - 1
            steps_to_advance += 1
        #print "Current array status is " +  str(instructions)
        #print "Next index to jump to is " + str(i)





    print "Number of steps for exiting " + str(steps_to_advance)
