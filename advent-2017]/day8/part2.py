from __future__ import division
import operator
import math
import json
import pprint


#Input:
# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10

ops = {
    "+": operator.add,
    "-": operator.sub,
    ">" :operator.gt ,
    ">=" :operator.ge ,
    "==": operator.eq,
    "!=": operator.ne,
    "<": operator.lt,
    "<=": operator.le,
    "inc": operator.add,
    "dec": operator.sub
    }

with open('part1.txt') as f:
    variables = []
    comparator = []
    function = []
    variable_for_comparison = []
    operator = []
    denominator = []
    denominator_eol = " "
    values_dict = {}
    for line in f:
        if line:
            line_string_array =  line.split(" ")
            variables.append(line_string_array[0])
            comparator.append(int(line_string_array[2]))
            function.append(line_string_array[1])


            variable_for_comparison.append(line_string_array[4])
            operator.append(line_string_array[5])
            denominator_eol = line_string_array[6]
            denominator.append(denominator_eol[0:len(denominator_eol)-1])


    all_the_variables = set(variables)
    for variable in all_the_variables :
        values_dict[variable] = 0


    current_max = 0
    #How many operations we need to compute
    for i in range(0,len(variables)):
        if ops[operator[i]](  int(values_dict[variable_for_comparison[i]]) ,  int(denominator[i]) ) == True:
            value_to_be_added = 0
            value_to_be_added = ops[ function[i] ]( values_dict[variables[i]] , comparator[i] )
            values_dict[ variables[i] ] = value_to_be_added
            if values_dict[ variables[i] ] > current_max:
                current_max = values_dict[ variables[i] ]



    print "Final Dict is "
    pprint.pprint(values_dict)


    max_value = max(values_dict.values())
    print "Max value is " + str(max_value)


    print "Maximum value through the processing was " + str(current_max)
