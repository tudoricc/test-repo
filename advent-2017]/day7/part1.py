from __future__ import division
import math

import json

import pprint


#(0) 3  0  1  -3
#29629538
with open('part1.txt') as f:
    instructions = []
    tree_of_towers = {}
    current_pos_in_tree = 0
    for line in f:
#        print line

        if line:            # lines (ie skip them)
            line_string_1 =  line.split("\n")
            line_string =  line_string_1[0].split("->")
            #for number in line_string:
                #print "Part is + " + str(number)

            #if we have sub-towers length of array must be greater than 2
            if (len(line_string) == 1) :
                tree_of_towers[line_string[0].split(" ")[0] ] = []
            else:
                partial_list = line_string[1].split(",")
                final_list = [e[1:] for e in partial_list]
                tree_of_towers[line_string[0].split(" ")[0] ] = final_list

    print "Initial  Tree looks like this"
    #pprint.pprint(tree_of_towers)
    for dict_key in tree_of_towers.keys():
        for dict_key_different in tree_of_towers.keys():
            if dict_key != dict_key_different :

                if dict_key in tree_of_towers[dict_key_different]:

                    if len(tree_of_towers[dict_key]) > 1:
                        tree_of_towers[dict_key_different].remove(dict_key)
                        tree_of_towers[dict_key_different].append(tree_of_towers[dict_key])

                        tree_of_towers.pop(dict_key)



    print "Final  Tree looks like this"
    for key in tree_of_towers.keys():
        if len(tree_of_towers[key]) == 0:
            tree_of_towers.pop(key)

    #pprint.pprint(tree_of_towers)
    print "Biggest one is:"
    for key in tree_of_towers.keys() :
        print "For key "+ str(key) + " the length is " + str(len(tree_of_towers[key]))
