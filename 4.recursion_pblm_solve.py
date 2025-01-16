s="Assalamualikum"

for i in s:
    print(i)
print("000000")


for i in range(-1, -len(s)-1, -1): #reverse order
    print(s[i])

print("000000")    

for i in s[::-1]: #reverse order another way
    print(i)

print("000000") 

def rcs(s):  #recursive function
    if len(s)>0:
        print(s[0])
        rcs(s[1:])

rcs("Assalamualikumyou") #recursive call

def rcs(s):  #recursive function
    if len(s)>0:
        rcs(s[1:])
        print(s[0])

rcs("Assalamualikumyou") #recursive call