from __future__ import division
import math
import json
import pprint

with open('part2.txt') as f:
    instructions = []
    tree_of_towers = {}
    tree_of_weight = {}
    current_pos_in_tree = 0
    for line in f:

        #I realise I could've used a tree structure but I wanted to keep it as simple as possible[data structure wise]
        #You will not think so after you read the code below :)
        if line:            # lines (ie skip them)
            line_string_1 =  line.split("\n")
            line_string_with_space =  line_string_1[0].split("->")

            if (len(line_string_with_space) == 1) :
                tree_of_towers[line_string_with_space[0].split(" ")[0] ] = {}
                tree_of_towers[line_string_with_space[0].split(" ")[0] ]['weight'] = 0

                tree_of_towers[line_string_with_space[0].split(" ")[0] ]['weight'] = int(line_string_with_space[0].split(" ")[1].split("(")[1].split(")")[0])
                tree_of_towers[line_string_with_space[0].split(" ")[0] ]['neighbours'] = {0:[]}
                tree_of_weight[line_string_with_space[0].split(" ")[0] ]['weight'] =  0
                tree_of_weight[line_string_with_space[0].split(" ")[0] ]['weight'] = int(line_string_with_space[0].split(" ")[1].split("(")[1].split(")")[0])
                #tree_of_towers[line_string_with_space[0].split(" ")[0] ]['neighbours'] = []
            else:
                tree_of_towers[line_string_with_space[0].split(" ")[0] ] = {}
                tree_of_towers[line_string_with_space[0].split(" ")[0] ]['weight'] = 0

                tree_of_towers[line_string_with_space[0].split(" ")[0] ]['weight'] = int(line_string_with_space[0].split(" ")[1].split("(")[1].split(")")[0])
                partial_list = line_string_with_space[1].split(",")
                final_list = [e[1:] for e in partial_list]
                tree_of_towers[line_string_with_space[0].split(" ")[0] ] ['neighbours'] = {}
                tree_of_towers[line_string_with_space[0].split(" ")[0] ] ['neighbours'] = {0:final_list}
                #this is something you need to calculate
                tree_of_towers[line_string_with_space[0].split(" ")[0] ] ['neighbours-weight'] = 0


    # print "Initial  Tree looks like this"
    #pprint.pprint(tree_of_towers)


    for dict_key in tree_of_towers.keys():
        for dict_key_different in tree_of_towers.keys():
            #iterate through the dict keys to see if the current key is a "child" node
            if dict_key != dict_key_different :
                # if the node we are searching for is in the list of parent's neighbours then
                # I remove it from the list of neighbours and add the child- neighbours
                # to the list of part-neighbours
                if dict_key in tree_of_towers[dict_key_different]['neighbours'][0]:
                    if len(tree_of_towers[dict_key]['neighbours'][0]) > 1:

                        if dict_key in tree_of_towers[dict_key_different]['neighbours'][0]:
                            tree_of_towers[dict_key_different]['neighbours'][dict_key] = tree_of_towers[dict_key]['neighbours'][0]
                            tree_of_towers[dict_key_different]['neighbours'][0].remove(dict_key)

                        tree_of_towers[dict_key_different]['neighbours-weight'] += tree_of_towers[dict_key]['weight']
                        #I am not removing it here So I can itrate throught the items once and once and once more
                    else:
                        #This is a special case when the node we are looking for doesn't have any child nodes as well,
                        #My solution here is just to remove it and be done with it after I add it's "Weight"
                        tree_of_towers[dict_key_different]['neighbours-weight'] += tree_of_towers[dict_key]['weight']
                        tree_of_towers.pop(dict_key)


    #find weight of children + children's children

    # for tower in tree_of_towers.keys():
    #     if neighbours in tree_of_towers[tower]['neighbours']{0} =[]:
    #         tree_of_towers[tower]['neighbours'].pop(0)
    #     for neighbours in tree_of_towers[tower]['neighbours'].keys() :
    #         #If it has children then go to it's tree
    #         # This means it has children
    #         if not tree_of_towers[neighbours]:
    #
    #         else:

    #so pretty much Here is where I don't know what to do next,even with the basic example
    print "Final  Tree looks like this"

    pprint.pprint(tree_of_towers)
