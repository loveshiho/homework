name = "hello world"
print(name)
print(f'字符串的长度为：{len(name)}，字母o出现的次数为：{name.count("o")}')
namelist = name.split(" ")
print(namelist)
name1 = "12hollo21"
name2 = name1.strip("21")
print(name2)