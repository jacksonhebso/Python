# Program that calculates the distance between any two points on the Earth’s surface
# given their latitude and longitude

from math import radians, sin, cos, acos #imports math library module

# Print command outputs values to screen
print('This program allows the user to calculate the distance between two points on the globe.')
print('Remember northern latitudes and eastern longitudes are positive numbers, while southern latitudes and western longitudes are negative numbers.')
 

# Print command outputs values to screen
print('Input coordinates of a point:')

# Assigned variables for the if statements
latitude1 = 0
longitude1 = 0
latitude2 = 0
longitude2 = 0

# The while statement keeps looping until its condition is met. 
while (latitude1 == 0):

# try statement attempts to execute each statement below.
# if try statement failed, it skips the remaining part and jumps to the except statement
    try:
        lat1 = float(input('Enter first latitude: '))
        
# The if command runs if the condition for latitude is met.  
        if lat1 == 0: # condition is met if variable is 0
            print('That location is on the equator.')
            latitude1 = 1 # if condition is met the program proceeds to longitude input.
        if lat1 > 0 and lat1 <= 90: # condition is met if variable is between 1-90
            print('That location is north of the equator.')
            latitude1 = 1
        if lat1 >= -90 and lat1 < 0: # condition is met if variable is between -90 and -1
            print('That location is south of the equator.')    
            latitude1 = 1
        if lat1 > 90: # condition is met if variable is greater than 90, loops back to try again
            print('That location does not have a valid latitude!')
        if lat1 < -90: # condition is met if variable is less than -90, loops back to try again
            print('That location does not have a valid latitude!')
    
# If the conversion failed, the except statement will give an error message
    # and continue to a new loop.
    except:
        print('Invalid input. Please try again.')
    
# The while statement keeps looping until its condition is met. 
while (longitude1 == 0):

# try statement attempts to execute each statement below.
# if try statement failed, it skips the remaining part and jumps to the except statement
    try:
        lon1 = float(input('Enter first longitude: '))

        if lon1 == 0: # condition is met if variable is 0
            print('That location is on the prime meridian.')
            longitude1 = 1 #program ends if this condition is met.
        if lon1 > 0 and lon1 <= 180: # condition is met if variable is between 1-180
            print('That location is east of the prime meridian.')
            longitude1 = 1
        if lon1 >= -180 and lon1 < 0: # condition is met if variable is between -180 and -1
            print('That location is west of the prime meridian.')
            longitude1 = 1
        if lon1 > 180: # condition is met if variable is greater than 180, loops back to try again
            print('That location does not have a valid longitude!')

        if lon1 < -180: # condition is met if variable is less than -180, loops back to try again
            print('That location does not have a valid longitude!')

# If the conversion failed, the except statement will give an error message
    # and continue to a new loop.
    except:
        print('Invalid input. Please try again.')

while (latitude2 == 0):

# try statement attempts to execute each statement below.
# if try statement failed, it skips the remaining part and jumps to the except statement
    try:
        lat2 = float(input('Enter second latitude: '))
        
# The if command runs if the condition for latitude is met.  
        if lat2 == 0:
            print('That location is on the equator.')
            latitude2 = 1 # if condition is met the program proceeds to longitude input.
        if lat2 > 0 and lat2 <= 90: # condition is met if variable is between 1-90
            print('That location is north of the equator.')
            latitude2 = 1
        if lat2 >= -90 and lat2 < 0: # condition is met if variable is between -90 and -1
            print('That location is south of the equator.')    
            latitude2 = 1
        if lat2 > 90: # condition is met if variable is greater than 90,loops back to try again
            print('That location does not have a valid latitude!')
        if lat2 < -90: # condition is met if variable is less than -90, loops back to try again
            print('That location does not have a valid latitude!')
    
# If the conversion failed, the except statement will give an error message
    # and continue to a new loop.
    except:
        print('Invalid input. Please try again.')
    
# The while statement keeps looping until its condition is met
while (longitude2 == 0):

# try statement attempts to execute each statement below.
# if try statement failed, it skips the remaining part and jumps to the except statement
    try:
        lon2 = float(input('Enter second longitude: '))

        if lon2 == 0: # condition is met if variable is 0
            print('That location is on the prime meridian.')
            longitude2 = 1 # program ends if this condition is met
        if lon2 > 0 and lon2 <= 180: # condition is met if variable is between 1-180
            print('That location is east of the prime meridian.')
            longitude2 = 1 
        if lon2 >= -180 and lon2 < 0: # condition is met if variable is between -180 and -1
            print('That location is west of the prime meridian.')
            longitude2 = 1
        if lon2 > 180: # condition is met if variable is greater than 180, loops back to try again
            print('That location does not have a valid longitude!')

        if lon2 < -180: # condition is met if variable is less than -180, loops back to try again
            print('That location does not have a valid longitude!')

# If the conversion failed, the except statement will give an error message
    # and continue to a new loop.
    except:
        print('Invalid input. Please try again.')


#formulas to run calculation of distance between two points on the earth's surface

firstlat = radians(lat1)
firstlon = radians(lon1)
    
secondlat = radians(lat2)
secondlon = radians(lon2)
    

dist = 6371 * acos(sin(firstlat)*sin(secondlat) + cos(firstlat)*cos(secondlat)*cos(firstlon - secondlon))
print("The distance is %.f km." % dist)

    
