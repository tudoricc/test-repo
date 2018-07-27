from __future__ import division
import math
#import numpy as np
a={}
a[(0,0)] = 1
copy_a = {}
copy_a[(0,0)] = 1
#>>> a = np.array([[0, 1], [2, 3]], order='F')
#>>> a.resize((2, 1))
#>>> a
#>>     >>> import math
#>>     >>> print(math.pow(4,4))

# 17	16	15	14	13
# 18	5	4	3	12
# 19	6	1	2	11
# 20	7	8	9	10
# 21	22	23	24	25
#array([[0],
# 1 ,3 ,5 ,7 elemeents in a row/coll
# copy_array={}
old_val = 1
for step in range(2,3):
    old_val = old_val + 2
    #ranges = [(n, min(n+step, stop)) for n in xrange(start, stop, step)]
    for i in range(0,step+1):
        for j in range(0,step+1):
            copy_a[(i,j)] = 0
    copy_a[(0,0)] = 1+ math.pow(4,step-1)
    copy_a[(step-1,step-1)] = a[(step-2,step-2)]
    copy_a[(step,step)] = math.pow(old_val,2)

    a = copy_a

print a
