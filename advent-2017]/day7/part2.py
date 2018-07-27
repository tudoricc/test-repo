from __future__ import division
import math

import json

import pprint

def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))
#(0) 3  0  1  -3
#29629538
with open('part2.txt') as f:
    instructions = []
    tree_of_towers = {}
    current_pos_in_tree = 0
    for line in f:
#        print line

        if line:            # lines (ie skip them)
            line_string_1 =  line.split("\n")
            line_string_with_space =  line_string_1[0].split("->")

            if (len(line_string_with_space) == 1) :
                tree_of_towers[line_string_with_space[0].split(" ")[0] ] = {}
                tree_of_towers[line_string_with_space[0].split(" ")[0] ]['weight'] = 0

                tree_of_towers[line_string_with_space[0].split(" ")[0] ]['weight'] = int(line_string_with_space[0].split(" ")[1].split("(")[1].split(")")[0])
                tree_of_towers[line_string_with_space[0].split(" ")[0] ]['neighbours'] = {}
                tree_of_towers[line_string_with_space[0].split(" ")[0] ]['neighbours']['tree'] = []
            else:
                tree_of_towers[line_string_with_space[0].split(" ")[0] ] = {}
                tree_of_towers[line_string_with_space[0].split(" ")[0] ]['weight'] = 0

                tree_of_towers[line_string_with_space[0].split(" ")[0] ]['weight'] = int(line_string_with_space[0].split(" ")[1].split("(")[1].split(")")[0])
                partial_list = line_string_with_space[1].split(",")
                final_list = [e[1:] for e in partial_list]
                tree_of_towers[line_string_with_space[0].split(" ")[0] ] ['neighbours'] = {}
                tree_of_towers[line_string_with_space[0].split(" ")[0] ] ['neighbours']['tree'] = final_list
                #this is something you need to calculate
                tree_of_towers[line_string_with_space[0].split(" ")[0] ] ['neighbours-weight'] = 0


    # print "Initial  Tree looks like this"
    # pprint.pprint(tree_of_towers)



    for dict_key in tree_of_towers.keys():
        for dict_key_different in tree_of_towers.keys():
            if dict_key != dict_key_different :

                if dict_key in tree_of_towers[dict_key_different]['neighbours']['tree']:
                    #print "Gets here"
                    #if len(tree_of_towers[dict_key]['neighbours']) > 1:

                    if len(tree_of_towers[dict_key]['neighbours']['tree']) > 1:
                        #tree_of_towers[dict_key_different]['neighbours']['tree'].remove(dict_key)
                        #tree_of_towers[dict_key_different]['neighbours']['tree'][tree_of_towers[dict_key_different]['neighbours']['tree'].index(dict_key)] = tree_of_towers[dict_key]['neighbours']['tree']
                        #tree_of_towers[dict_key_different]['neighbours']['tree'][tree_of_towers[dict_key]] = tree_of_towers[dict_key]['neighbours']['tree']
                        for neighbour_index in range(0,len(tree_of_towers[dict_key_different]['neighbours']['tree'])):
                            if tree_of_towers[dict_key_different]['neighbours']['tree'][neighbour_index] == dict_key:
                                tree_of_towers[dict_key_different]['neighbours']['tree'][neighbour_index][dict_key] = tree_of_towers[dict_key]['neighbours']['tree']

                        tree_of_towers[dict_key_different]['neighbours-weight'] += tree_of_towers[dict_key]['weight']
                        #tree_of_towers.pop(dict_key)
                    else:
                        #do not remove the node
                        #tree_of_towers[dict_key_different]['neighbours']['tree'].remove(dict_key)

                        #tree_of_towers[dict_key_different]['neighbours']['tree'][tree_of_towers[dict_key]] = tree_of_towers[dict_key]['neighbours']
                        tree_of_towers[dict_key_different]['neighbours-weight'] += tree_of_towers[dict_key]['weight']
                        tree_of_towers.pop(dict_key)


    current_size_of_tree = len(tree_of_towers)

    #find parent_node
    max_nodes_count =0
    for dict_key in tree_of_towers.keys():
        tree_of_towers[dict_key]['weight'] += tree_of_towers[dict_key]['neighbours-weight']



    for dict_key in tree_of_towers.keys():
        print "-------------------------------------------"
        print "For node " + str(dict_key) + " we have the total weight of " + str(tree_of_towers[dict_key]['weight'])
        print "-------------------------------------------"
    #fbgguv is the winning node


#Iterate untill you have 2 remaining nodes
#TODO find the maximum/parent node

    # while current_size_of_tree > 1:
    #
    #     for dict_key in tree_of_towers.keys():
    #         for dict_key_different in tree_of_towers.keys():
    #             if dict_key != dict_key_different :
    #
    #
    #     current_size_of_tree -= 1

    print "Final  Tree looks like this"
    # for key in tree_of_towers.keys():
    #     if len(tree_of_towers[key]['neighbours']) == 0:
    #         tree_of_towers.pop(key)

    pprint.pprint(tree_of_towers)

    # ugml + (gyxo + ebii + jptl) = 68 + (61 + 61 + 61) = 251
    # padx + (pbga + havc + qoyq) = 45 + (66 + 66 + 66) = 243
    # fwft + (ktlj + cntj + xhth) = 72 + (57 + 57 + 57) = 243
    # for dict_key in tree_of_towers.keys():
    #     for dict_key_different in tree_of_towers.keys():
    #         if dict_key != dict_key_different :
    #
    #             if dict_key in tree_of_towers[dict_key_different]['neighbours'] :
    #
    #                 if len(tree_of_towers[dict_key]['neighbours']) > 1:
    #                     tree_of_towers[dict_key_different].remove(dict_key)
    #                     tree_of_towers[dict_key_different].append(tree_of_towers[dict_key]['neighbours'])
    #
    #                     tree_of_towers.pop(dict_key)
    #                 elif len(tree_of_towers[dict_key]['neighbours']) == 1:
    #                     tree_of_towers[dict_key_different]['neighbours'].remove(dict_key)
    #                     tree_of_towers[dict_key_different].append(tree_of_towers[dict_key]['neighbours'])
    #                     tree_of_towers[dict_key_different]['neighbours-weight'] += int(tree_of_towers[dict_key]['weight'])
    #                     tree_of_towers.pop(dict_key)
    #
    # print
    # print "---------------------------------------"
    # print "Final  Tree looks like this"
    #
    #
    # pprint.pprint(tree_of_towers)
