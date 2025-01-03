# f= open("test.txt" , "r")
# print(f)
# f.close()

with open("test.txt" , "r") as f:
    #print(f.read())
    #print(f.read(50))
    #print("yyy\n")
    #print(f.read(20))
    #print(f.readline())
    count=1
    for i in f:    
      if count>4:
        break
      print(i)
      count+=1
