#! /usr/bin/env/ python3

cities={"Ahmedabad":"380001", "Aizawal":"796001", "Amritsar":"143001","Bangalore":"560001","Bhopal":"462001","Bhubaneswar":"751001", "Kolkata":"700001","Imphal":"795001"}

#printing the dictionary
print("Printing cities: \n{}\n".format(cities))

#delete a dictionary item
del(cities["Ahmedabad"])
print("Printing cities after deleting an item: \n{}\n".format(cities))

#delete the dictionary
del(cities)

#print the dictionary:
print("Printing deleted dictionary: \n{}\n".format(cities))
