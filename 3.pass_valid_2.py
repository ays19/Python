#Password Validation
password = input()
if(len(password)<8):
   print("Invalid")
   print("Not enough length")
else:
   uppr =0
   lower = 0
   digit = 0
   special = 0
   for i in password:
      if "A"<=i<="Z":
         uppr = uppr+1
      elif "a"<=i<="z":
         lower = lower+1
      elif "0"<=i<="9":
         digit+=1
      elif i in"!@#$%^&*_":
         special+=1

   if(uppr>0 and lower>0 and digit>0 and special>0):
      print("Valid Password")
   else:
      print("Invalid Password")
      if(uppr==0):
         print("Upper case Missing")
      elif(lower==0):
         print("Lower case Missing")
      elif(digit==0):
         print("Digit Missing")
      elif(special==0):
         print("Special case Missing")
