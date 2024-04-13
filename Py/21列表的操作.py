name1 = [1,2,3,4,5,6,7,8,9,10]
name2 = []
name3 = []
i=0
print(len(name2))
while(i<len(name1)):
    if name1[i]%2 == 0:
        name2.append(name1[i])
    else:
        name3.append(name1[i])
    i+=1
print(f"偶数集：{name2},奇数集：{name3}")