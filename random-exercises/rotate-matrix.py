input_matrix = [ [1,2,3],[4,5,6],[7,8,9]]


#Given  an  image  represented  by  an  NxN  matrix,  where  each  pixel  in  the  image  is  4
#bytes, write a method to rotate the image by 90 degrees Do that in place
print len(input_matrix)
print input_matrix

#for line_count in len(input_matrix)
output_matrix = input_matrix

current_line_index = 0
current_collumn_index = len(input_matrix) - 1
no_of_changes = 0
# while no_of_changes < (pow(len(input_matrix),2)):
#     #print line_count
#     #current_location = len(input_matrix) - 1
#
#
#     old_value = input_matrix[current_line_index][current_line_index]
#     output_matrix[current_line_index][current_collumn_index] = input_matrix[current_line_index][current_line_index]
#     output_matrix[current_line_index][current_line_index] = input_matrix[current_collumn_index][current_collumn_index]
#     no_of_changes += 1
#
#     current_line_index = ( current_line_index + 1 ) % len(input_matrix)
#     current_collumn_index = (current_collumn_index + 1) % len(input_matrix)

current_pos = 0
for current_collumn_index in range(len(input_matrix)-1,-1,-1):


    for current_line_index in range(0,len(input_matrix),1):
        output_matrix[current_line_index][current_collumn_index]=input_matrix[current_pos][current_line_index]
    current_pos += 1

print output_matrix
