from __future__ import division
import math

a={}
a[(0,0)] = 1
copy_a = {}
copy_a[(0,0)] = 1

# 17	16	15	14	13
# 18	5	4	3	12
# 19	6	1	2	11
# 20	7	8	9	10
# 21	22	23	24	25 26
#....                  49
#array([[0],
# 1 ,3 ,5 ,7 elemeents in a row/coll
# copy_array={}


# Go 1024 steps


# a[i][i] = sqrt
float_sqrt = math.sqrt(361527)
#SO I WILL NEED A DICT OF  int(float_sqrt)

#Start with the middle
a[(int(float_sqrt)/2,int(float_sqrt)/2)] = 1
i =  int(float_sqrt)/2
j = int(float_sqrt)/2

for i in range(0,602):
    for j in range(0,602):
        a[(i,j)] = 0

not_built = False
step = 3
while not_built != True :
    #move to the right
    for k in range(0,step) :
        a[((i,j+1))] = a[(i,j + 1)] + a[(i,j - 1)] + a[(i + 1,j)] + a[(i - 1,j)] + a[(i + 1,j + 1)] + a[(i + 1,j - 1)] + a[(i - 1,j + 1)] + a[(i - 1,j - 1)]

    #move to the up
    for k in range(0,step) :
        a[(i-1,j)] = a[(i,j + 1)] + a[(i,j - 1)] + a[(i + 1,j)] + a[(i - 1,j)]+ a[(i + 1,j + 1)] + a[(i + 1,j - 1)] + a[(i - 1,j + 1)] + a[(i - 1,j - 1)]
    #Move to the left
    for k in range(0,step):
        a[(i,j-1)] = a[(i,j + 1)] + a[(i,j - 1)] + a[(i + 1,j)] + a[(i - 1,j)]+ a[(i + 1,j + 1)] + a[(i + 1,j - 1)] + a[(i - 1,j + 1)] + a[(i - 1,j - 1)]

    #move to the down
    for k in range(0,step) :
        a[(i+1,j)] = a[(i,j + 1)] + a[(i,j - 1)] + a[(i + 1,j)] + a[(i - 1,j)]+ a[(i + 1,j + 1)] + a[(i + 1,j - 1)] + a[(i - 1,j + 1)] + a[(i - 1,j - 1)]




    step += 1
    if step == 3:
        not_built = True


pprint.pprint(a)
