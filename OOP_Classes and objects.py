class patient:
    def __init__(self, name, age, bg): # Constructor
        self.name = name
        self.age = age  # Instance variable
        self.bg = bg
        
p1 = patient("John", 25, "O+")
p2 = patient("Amin", 21, "AB-")

print(p1.name, p1.age, p1.bg)
print(p2.name)
