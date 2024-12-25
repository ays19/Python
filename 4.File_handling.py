# f= open("test.txt" , "r")
# print(f)
# f.close()

with open("test.txt" , "r") as f:
    print(f.read())
    (f.read())