class patient:
    count=0 # Class variable
    def __init__(self, n, age, bg): # Constructor
        self.name = n  # Instance variable
        self.age = age  # Instance variable
        self.bg = bg # Instance variable
        patient.count += 1  # Accessing class variable

    def printInfo(self):
        print(f"Name: {self.name}\nAge: {self.age}\nBlood Group: {self.bg}")
        
p1 = patient("John", 25, "O+")
p2 = patient("Amin", 21, "AB-")

print(p1.name, p1.age, p1.bg)
print(p2.name)
print("000000")
p1.printInfo()
print(patient.count)