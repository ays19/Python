name ="Sharar"
name1 = "123"
name2 = "@#$"

print(name, name1, name2)
print(name+name1+name2)

print(name[0])
print(name[len(name)-1])
print(name[-1])
print(name[-len(name)])
print(name[0]+name[1]+name[2])
print(name[1:4]) #Slicing
print(name[1:4]+name[-6:]+name1[:2])

s= "Hello"
for i in s:
 if(i=="l"):
  print("Yes")
  break

print("l" in s)

