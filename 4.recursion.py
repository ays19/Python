def mA(x):
    print(x)
    if x <= 20:  # condition to stop the recursion
        mA(x + 1)  # Recursive call

mA(10)     
print("000000")
def mA(x):
    
    if x <= 20:  # condition to stop the recursion
        print(x)
        mA(x + 1)  # Recursive call

mA(10) 

print("000000")

def mA(x):
    
    if x <= 20:  # condition to stop the recursion
        
        mA(x + 1)  # Recursive call
        print(x)

mA(10)  