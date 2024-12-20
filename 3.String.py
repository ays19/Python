name ="Sharar"
name1 = "123"
name2 = "@#$"

# print(name, name1, name2)
# print(name+name1+name2)

# print(name[0])
# print(name[len(name)-1])
# print(name[-1])
# print(name[-len(name)])
# print(name[0]+name[1]+name[2])
# print(name[1:4]) #Slicing
# print(name[1:4]+name[-6:]+name1[:2])

# s= "Hello"
# for i in s:
#  if(i=="l"):
#   print("Yes")
#   break

# print("l" in s)

X= "ahsan Yasir Sharar"
idx = 0
for i in range(0, len(X)):
 if X[i]== "Y":
   idx= i
   break
print(i)
print(X[0:2]+X[idx:idx+2])


