num = int(input())
if (num % 2 == 0):
    print("Even\n")
else:
    print("Odd\n")


if(num == 0):
    print("Zero")
elif (num<0):
    print("negetive")
else:
    print("Positive")


#Multiple condition
if(num % 5==0 and num % 7==0):
    print("yes")
else:
    print("NO")

if num % 5 ==0 and num%7!=0:
    print("Yes")
elif num%5!=0 and num%7==0:
    print("Yes")
else:
    print("NO") 