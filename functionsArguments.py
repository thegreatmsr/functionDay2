#Types of Arguments
def greet(name, dept):
    print(f"Hi {name}")
    print(f"Are you from {dept} department")
    
greet("Jenny", dept="CS")  #Postional Arguments and then keywords Arguments

#Now we will learn about the default arguments


def greet(name, subject, dept ="CS"): #In this we have the department of the individual as CS as a default parameter 
    print(f"HI {name}")
    print(f"Do You Teach {subject}?")
    print(f"Are you from {dept} department")
greet("Jenny", subject="Hindi" ,dept="B.TECH CSE")
greet("Manav", subject="Maths")


#Now we study about the arbitary arguments this arguments can be used in various purpose like if we want to add 3 number instead of the 2 numbers 
'''def add (*numbers):(5,7,9,)
for i in numbers:
        c =c+i
    print(f"Sum is {c}")
add(5,7,9)'''

def add(*numbers):
    c =0
    for i in numbers:
       c = c+i 
    print(f"Sum is{c}")
add(5,7,9)
    
    