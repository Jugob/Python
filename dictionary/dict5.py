#! /usr/bin/env/ python3

cities={"Ahmedabad":"380001", "Aizawal":"796001", "Amritsar":"143001","Bangalore":"560001","Bhopal":"462001","Bhubaneswar":"751001", "Kolkata":"700001","Imphal":"795001"}

#printing the dictionary
print("Printing cities: \n{}\n".format(cities))

cities2={"Patna":"800001", "Chennai":"600094"}

#printing the dictionary
print("Printing cities2: \n{}\n".format(cities2))

#Adding 2 dictionaries:
cities.update(cities2)
print("Printing merged dictionary: \n{}\n".format(cities))
