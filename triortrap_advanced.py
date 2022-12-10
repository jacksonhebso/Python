# This program allows the user the ability to calculate the area of a triangle or trapezoid. If the user enters an
# invalid character,the program will try to convert to a numeric type. It will ask the user for an acceptable value up to 4 times. 

loopCount = 0
# The "while" statement keeps looping until its condition (loopCount<4) made False.
while loopCount<4:
    # loopCount will increase 1 for each loop
    loopCount += 1

# The print command prints the choices available to calculate area. 
    print("This program finds the area of a triangle or trapezoid.")
    print()
    print ("1. Triangle")
    print ("2. Trapezoid")
    print()


# Defined variable for x
    x = (0)

# The while statement keeps looping until its condition is met.
    while (x == 0): 
        # try statement attempts to execute each statement below.
        # if try statement failed, it skips the remaining part and jumps to the except statement
        try: 
            x = int(input("Please choose 1 or 2: ")) # The variable x is user input, 1 for triangle or 2 for trapezoid. 

# The if command runs if the condition for x is a number other than 1 or 2.
            if x < 1 or x > 2:   
                print('Invalid option. Please try again.')
                print ()
                loopCount<4 # only allows for invalid inputs up to 4 times.
                break # ends the program
        

# The if command allows the program to run the area calculation for a triangle. Once the condition is met.
            if x == 1:
                print('You have chosen to calculate the area of a triangle.')
                h = input('Please enter the height of the triangle. ')
                print('Your input is',h,'which has a type of',type(h))

# the float function attempts to convert the value of variable "h" and/or "b" into a float type.
                h = float(h)
                print('After a successful conversion, the type of "height" is now:',h,type(h))
                print()
                b = input('Please enter the base length of the triangle. ')
                print('Your input is', b, 'which has a type of', type(b))
                b = float(b)

# If the conversion was successful, "h" and/or "b" becomes a numeric type,
        # which could be used in any further calculation.
        # The while loop breaks after that.
                print('After a successful conversion, the type of "base length" is now:',b,type(b))
                print()
                area = 0.5 * h * b
                print("The area of a triangle with a height of", h, "and a base of", b, "is", area,".")
                loopCount=4

  

# The if command allows the program to run the area calculation for a trapezoid. Once the condtion is met.
            if x == 2:
                print('You have chosen to calculate the area of a trapezoid.')
                short_base = input('Please enter the length of the short base. ')
                print('Your input is', short_base, 'which has a type of', type(short_base))

# the float function attempts to convert the value of variable "short_base" into a float type.
                short_base = float(short_base)
                print('After a successful conversion, the type of "the short base" is now:',short_base,type(short_base))
                print()
                long_base = input('Please enter the length of the long base. ')
                print('Your input is', long_base, 'which has a type of', type(long_base))
# the float function attempts to convert the value of variable "long_base" into a float type.
                long_base = float(long_base)
                print('After a successful conversion, the type of "the long base" is now:',long_base,type(long_base))
                print()
                height = input('Please enter the height of the trapezoid. ')
                print('Your input is', height, 'which has a type of', type(height))
# the float function attempts to convert the value of variable "height" into a float type.
                height = float(height)
                print('After a successful conversion, the type of "the height" is now:', height,type(height))
                print()
                area = ((short_base + long_base) /2) * height
                print("The area of a trapezoid with the height of", height, ",a short base of", short_base, ",and a long base of", long_base, "is", area,".")
                loopCount=4               
        
             
# If user input has failed, the except statement will give an error message
    # and continue to a new loop until the loop count has reached 4.

        except:
            print('You entered a value that is not acceptable.')
            print()
            loopCount<4
            break
           

    
