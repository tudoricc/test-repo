def jump(position,num,problem_list):
    new_position=position+num
    if num >= 3:
            problem_list[position]=problem_list[position]-1
    else:
            problem_list[position]=problem_list[position]+1
    return new_position,problem_list

myfile = open('part2.txt', "r")
data=myfile.readlines()
problem_list=[]

for str_value in data:
        str_value=str_value.strip()
        int_value=int(str_value)
        problem_list.append(int_value)

target_position=len(problem_list)
current_position=0
counter=0

while current_position != target_position:
        new_position, problem_list=jump(current_position,problem_list[current_position],problem_list)
        counter+=1
        current_position=new_position
