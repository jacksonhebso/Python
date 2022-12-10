# This program is based on user input for latitude and longitude.
# Based on the variables entered, a statement will print as to where the coordinate is located on the earth's surface. 

# Print command outputs values to screen
print('Input coordinates of a point:')

# Assigned variables for the statements
latitude = 0
longitude = 0


# The while statement keeps looping until a defined condition below is met
while (latitude == 0):

# try statement attempts to execute each statement below
# if try statement failed, it skips all ifs below and jumps to the except statement
    try:
        lat = float(input('Enter latitude: '))
        lat = lat.split(',')

        if type(lat) is tuple:
            print('the input is in dms form,')
        
# The if command runs if the condition for latitude is met 
        if lat == 0: #condition is met if variable is 0
            print('That location is on the equator.')
            latitude = 1 # if condition is met the program proceeds to longitude input.
        if lat > 0 and lat <= 90: # condition is met if variable is between 1-90
            print('That location is north of the equator.')
            latitude = 1
        if lat >= -90 and lat < 0: # condition is met if variable is between -90 and -1
            print('That location is south of the equator.')    
            latitude = 1
        if lat > 90: # condition is met if variable is greater than 90
            print('That location does not have a valid latitude!')
        if lat < -90: # condition is met if variable is less than -90
            print('That location does not have a valid latitude!')
    
# If the conversion failed, the except statement will give an error message
    # and continue to a new loop.
    except:
        print('Invalid input. Please try again.')
    
# The while statement keeps looping until its condition is met. 
while (longitude == 0):

# try statement attempts to execute each statement below.
# if try statement failed, it skips the remaining part and jumps to the except statement
    try:
        lon1 = float(input('Enter longitude: '))

        if lon1 == 0:
            print('That location is on the prime meridian.')
            longitude = 1 #program ends if this condition is met for if statements
        if lon1 > 0 and lon1 <= 180: # condition is met if variable is between 1-180
            print('That location is east of the prime meridian.')
            longitude = 1 
        if lon1 >= -180 and lon1 < 0: # condition is met if variable is between -180 and -1
            print('That location is west of the prime meridian.')
            longitude = 1
        if lon1 > 180: # condition is met if variable is greater than 180
            print('That location does not have a valid longitude!')

        if lon1 < -180: # condition is met if variable is less than -180
            print('That location does not have a valid longitude!')

# If the conversion failed, the except statement will give an error message
    # and continue to a new loop.
    except:
        print('Invalid input. Please try again.')
