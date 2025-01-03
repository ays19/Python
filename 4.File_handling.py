# f= open("test.txt" , "r")
# print(f)
# f.close()

with open("test.txt" , "r") as f:
    #print(f.read())
    #print(f.read(50))
    #print("yyy\n")
    #print(f.read(20))
    #print(f.readline())

    # count=1
    # for i in f:    
    #   if count>4:
    #     break
    #   print(i)
    #   count+=1

    l1=[]
    for i in f:
        l1.append(i)
    print(l1)
    print("ooo\n")
    for i in range(3,6):
        print(l1[i])  
