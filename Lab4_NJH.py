
#import csv, math, and sys modules for required functions in program 
import csv
import math
import sys

#fileName is defined as CityPop.csv. CityPop.csv opens as read only.  
fileName = 'CityPop.csv'
try:
    citypop = open(fileName,'r')
#System exits if unable to find CityPop.csv.
except:   
    print('Unable to open ' + fileName)
    sys.exit()

#citypop_file is a dictionary reader for CityPop.csv
citypop_file = csv.DictReader(citypop)

#class City: is a class that stores __init__ = instances. 
class City:
    def __init__(self, idfield, city_name, city_label, latitude, longitude, pop):
        self.idfield = idfield
        self.city_name = city_name
        self.city_label = city_label
        self.latitude = latitude
        self.longitude = longitude
        self.pop = pop

    
    def printCityAttributes(self): #function to print city attributes. Test example: City.printCityAttributes(cities[13])
        print(self.__dict__)

    def printDistance(self, othercity): #function to calculate distance between 2 cities. Test example: cities[14].printDistance(cities[4])
        latitudeA = math.radians(self.latitude)
        longitudeA = math.radians(self.longitude)
        latitudeB = math.radians(othercity.latitude)
        longitudeB = math.radians(othercity.longitude)
        distance = math.acos((math.sin(latitudeA)*math.sin(latitudeB))+(math.cos(latitudeA)*math.cos(latitudeB)*math.cos(longitudeA-longitudeB)))
        totalDistance = distance * 6371
        print('The distance between', self.city_label, 'and', othercity.city_label, 'is',
                  "{0:.4f}".format(totalDistance), 'km.')

    def printPopChange(self, year1, year2): #function to calculate population change between 2 years. Test example: cities[10].printPopChange(1975,2010)
        print('Population change in', self.city_label, 'from', year1, 'to', year2, 'is', "{0:.4f}".format(self.pop[year2] - self.pop[year1]),'million.')

#empty cities list to store city instances
cities = []

#containers for storing data
for record in citypop_file:
    idfield = record['id']
    city_name = record['city'].replace('_',' ').title() #underscores will be removed for user readability, converts to titlecase
    city_label = record['label'].title() #converts to titlecase
    pop1970 = record['yr1970']
    pop1975 = record['yr1975']
    pop1980 = record['yr1980']
    pop1985 = record['yr1985']
    pop1990 = record['yr1990']
    pop1995 = record['yr1995']
    pop2000 = record['yr2000']
    pop2005 = record['yr2005']
    pop2010 = record['yr2010']
    lat = record['latitude']
    lon = record['longitude']
    pop = {} #storing a dictionary within a dictionary to search population values by year
    pop[1970] = float(pop1970)
    pop[1975] = float(pop1975)
    pop[1980] = float(pop1980)
    pop[1985] = float(pop1985)
    pop[1990] = float(pop1990)
    pop[1995] = float(pop1995)
    pop[2000] = float(pop2000)
    pop[2005] = float(pop2005)
    pop[2010] = float(pop2010)
    
    #next_city is appended to the cities list to view all attributes
    next_city = (City(idfield, city_name, city_label, float(lat), float(lon), pop))
    cities.append(next_city)

#closes Citypop.csv
citypop.close()

#prints attributes for all cities 
for C in cities:
    C.printCityAttributes()
