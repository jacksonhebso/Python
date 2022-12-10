#Program to convert latitude or longitude values to DMS or DD formats. 

#imports math module
import math 

#formula for converting dms to dd
def dms2dd(degrees, minutes, seconds, sign):
    dd = sign * float(degrees) + float(minutes)/60 + float(seconds)/(60*60)
    return dd

#formula for converting dd to dms
def dd2dms(DD_Value):
    d = int(deg)
    md = abs(deg - d)*60
    m = int(md)
    sd = (md - m) *60
    return [d,m,sd]

# Assigned variable for statements
convert = 0 
neg_1 = 0
neg_2 = 0

while (convert == 0): #if while = true, continues to while loop
    
    try:
        coord = input('Please enter a latitude or longitude value in DMS or DD format: ') #collect input from user
        coord_split = coord.split(',') #splits input string to list, for example 30,30,0 becomes '30','30','0'
        

        if len(coord_split)>1: #if input list variables are greater than 1, program continues to convert DMS to DD.
            print('The coordinate entered is in DMS form.') #also continues if input is invalid: text/characters 
            coord_split = [float(i) for i in coord_split] #converts coord_split from list to float
            convert = 1 #assigned variable is met, continues conversion.

            if (coord_split[0])<0: #if 1st character in coord_split list is less than 0, all characters in list become negatives. 
                neg_1 = coord_split[1]* -1 #neg_1 converts coord_split[1] to negative value
                neg_2 = coord_split[2]* -1 #neg_2 converts coord_split[2] to negative value

                #assigned variables for dmstodd formula for negative values
                degrees = coord_split[0]
                minutes = neg_1
                seconds = neg_2
                #dmstodd formula
                dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60) 
                print ('That coordinate is' ,(dd), 'in decimal degrees.')
                break 

            else: #if 1st character in coord_split is greater than 0, all characters remain positive.

                #assigned variables for dmstodd formula for positive values 
                degrees = coord_split[0]
                minutes = coord_split[1]
                seconds = coord_split[2]
                #dmstodd formula
                dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60) 
                print ('That coordinate is' ,(dd), 'in decimal degrees.')
                break
                
              

        if len(coord_split)==1: #if input list variables are equal to 1, program continues to convert DD to DMS.
            print('The coordinate entered is in DD form.') #also continues if input is invalid: text/characters 
            coord_split = [float(i) for i in coord_split] #converts coord_split from list to float
            convert = 2 #assigned variable is met, continues conversion. 

            #defined variables and formula to convert dd to dms
            dd = coord_split[0]
            deg1 = int(dd)
            md = abs(dd - deg1)*60
            min1 = int(md)
            secs1 = (md - min1)*60
            print ('That coordinate is',(deg1),(min1),round(secs1,4),'in Degrees Minutes Seconds. ') 
            break           

    except: #catches invalid values
            print ('Please enter a valid longitude or latitude to calculate.')
            break




            
