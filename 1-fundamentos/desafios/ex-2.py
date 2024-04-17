name = 'ana clara'
primary_name = name[0]

new_name = primary_name[0] + name.replace(primary_name,"$")[1:]

print(new_name)


str1 = 'henry'
str2 = 'franz'

str1_new = str2[0:2] + str1[2:]
str2_new = str1[0:2] + str2[2:]

print(str1_new)
print(str2_new)
