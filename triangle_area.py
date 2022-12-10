# This program calculates the area of a triangle.


print("This program finds the area of a triangle.") # Prints the message in green. 
print() # Prints a return. 

# The code below allows a user to enter a float integer for the height and base of a triangle.
# The user inputs the height and base when prompted.
height = float(input("Please enter the height of the triangle: "))
base = float(input("Please enter the base length of the triangle: "))

# The formula below is used to find the area of a triangle by multiplying the height and base by 0.5.
area = 0.5 * height * base

# This code block outputs the message in green below, to include the numbers inputed for height and base,
# and the result of our area calculation by using the formula above.
print("The area of a triangle with height", height, "and base", base, "is", area, ".")
