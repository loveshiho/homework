name = "学python，来黑马程序员，月薪过万"
name1 = name[::-1]
print(name1)
i = name1.index("黑")
j = name1.index("员")-1
print(i)
name2 = name1[i:j:-1]
print(name2)