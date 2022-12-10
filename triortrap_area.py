# This program calculates the area of a triangle or trapezoid.

#Formulas for calculating area

def triangle (h, b):
    area = 0.5 * h * b
    return area

def trapezoid (short_base, long_base, height):
    area = ((short_base + long_base) /2) * height
    return area


# The print command prints the message in green.
print("This program finds the area of a triangle or trapezoid.")
print() #Prints a return. 
print ("1. Triangle")
print ("2. Trapezoid")
print ("3. Quit")
print() #Prints a return. 


# The variable x is user input, 1 for triangle, 2 for trapezoid, or 3 to quit. 
x = int(input("Please enter 1, 2 or 3: "))

# The if command allows the program to run the calculation for the area of a triangle with user input. 
if x == 1:
    print('You have chosen to calculate the area of a triangle.') #Prints message in green. 
    h = float(input('Please enter the height of the triangle. ')) # Prompts user to enter in h=height of triangle.
    b = float (input ('Please enter the base length of the triangle. '))# Prompts user to enter in b=base of triangle.
    area = 0.5 * h * b  #Formula used to find the area of a triangle by multiplying the height and base by 0.5.
    print("The area of a triangle with a height of", h, "and a base of", b, "is", area,".") #Prints the area of a triangle.

# The elif command allows the program to run the calculation for the area of a trapezoid with user input. 
elif x == 2:
    print ('You have chosen to calculate the area of a trapezoid. ') #Prints message in green. 
    short_base = float(input('Please enter the length of the short base. ')) #Prompts user to enter short_base length of trapezoid. 
    long_base = float(input('Please enter the length of the long base. ')) #Prompts user to enter long_base length of trapezoid.
    height = float(input('Please enter the height of the trapezoid. ')) #Prompts user to enter height of trapezoid. 
    area = ((short_base + long_base) /2) * height #Formula used to find the area of a trapezoid.
    print ("The area of a trapezoid with the height of", height, ", a short base of", short_base, ",and a long base of", long_base, "is", area, ".") #Prints the area of a trapezoid.
    
# The elif command ends the program with a thank you. 
elif x == 3:
    print ('Thanks for playing! ')

