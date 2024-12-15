brand = str(input("Brand: "))
wheel = str(input("Wheel: "))
HP = int(input("Horse-Power: "))
sum = 0

if brand == "Ferrari":
    sum+= 30
elif brand =="Ford":
    sum+= 25
if wheel == "left":
    sum+=10
if HP > 2000:
    sum+= 10

print("Extra Tex: ", sum)