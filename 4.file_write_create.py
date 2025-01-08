#open an read the file after overwriting

f= open("test.txt" , "w")
f.write("This is a test file")
f.close()

#file creatiom
#fp = open("myfile.txt" , "x")
fp = open("myfile.txt" , "w")
fp.write("This is my new file")
fp.close()  #close the file