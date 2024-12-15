quiz = float(input("Quiz: "))
mid = float(input("MID: "))
final = float(input("Final: "))

sum = quiz+mid+final
print("Total marks: ", sum)

if sum >= 90:
    print("A")
elif sum >= 80 and sum <=89:
    print("B")
elif sum >= 70 and sum <=79:
    print("C")
elif sum >= 60 and sum <=69:
    print("D")
else:
    print("F")

    #2nd method
    
if sum >= 90:
    print("Grade: A")
elif  80 <= sum <=89:
    print("Grade: B")
elif 70 <= sum <=79:
    print("Grade: C")
elif 60 <= sum <=69:
    print("Grade: D")
else:
    print("Grade: F")
    