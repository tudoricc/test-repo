l = map(int,data.strip().split())

cycles = 0
prevs = []

while l not in prevs:
    prevs.append(l[:])
    m = max(l)
    i = l.index(m)
    l[i] = 0
    while m:
        i=(i+1)%len(l)
        l[i]+=1
        m-=1
    cycles+=1

print cycles
print len(prevs)-prevs.index(l)  #part 2
