print('Hello world!')

#variables
x=5
y="Sharar"
z=True

print(type(z))
print(type(y))
print(type(x))

#List
a = [5,6.7,"Saha", True, [41,"hi"]]
print(type(a))
print(a)
a[1]="hi"
a.append(True)
print(a[1])
print(a)
#Dictionary
b = {"Student1": "Ahsan", "Student": "yasir", "cgpa": 0.00}
print(b)
print(type(b))
print(b["Student1"])  
print(b["cgpa"])
b["cgpa"]=3.38
b["student3"]="AYS"
print(b)

#Tuple
b=(5,4,6,"hi",8)
print(b)

#Operator
x = 5**3
print(x)
y=10/3
print(y)
y=10//3  #floor division
print(y)

#Datatype conversion
print(4+5.5) #implicit conversion
print(int(10.77)) #explicit conversion
print(float(5)) #explicit conversion 
print(type(int("10")))  #explicit conversion
print("10"*5)
print(int("10")*5)  #explicit conversion

#Input
name = input("Enter your name: ")
print(name)
name = input()
print("Name:"+ name)

print("Sharar")

#practice
name1 = input("First name: ")
name2 = input("Last name: ")
name2 = "Rahman"
age = int(input("Age: "))
cgpa = float(input("Cgpa: "))
age= age -2
cgpa = cgpa+ 0.25
print("Name: " + name1 + " " + name2)
print("Age: ", age)
print("CGPA: " + str(cgpa))