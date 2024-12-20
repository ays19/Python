# def addition(a,b):
#     return a+b
# print(addition(2,3))
# print(addition(2,39))
# print(addition(26,3))
# print(addition(2,36))

# def difference(a,b):
#   if a>b:
#     return a-b
#   else:
#     return b-a
# print(difference(2,3))  
# print(difference(2,39))
# print(difference(26,3))
# print(difference(2,36))

# def number_range(st,end):
#   for i in range(st,end+1):
#    print(i)

# number_range(15,30)
# print(" ")
# number_range(5,10)
# print(" ")  
# number_range(3,3)

def divisibility(num):
  if num%6==0 and num%8==0 and num%12==0:
    return True
  else:
    return False
  
print(divisibility(24))
print(divisibility(7))