i=1
while i<10:
    j=1
    while j<i+1:
        print("%d*%d=%d\t"%(j,i,i*j),end='')
        j+=1
    i+=1
    print("\n")