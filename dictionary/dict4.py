#! /usr/bin/env/ python3

cities={"Ahmedabad":"380001", "Aizawal":"796001", "Amritsar":"143001","Bangalore":"560001","Bhopal":"462001","Bhubaneswar":"751001", "Kolkata":"700001","Imphal":"795001"}

#printing the dictionary
print(cities)

#printing value of key Bangalore
print("Print the values of the key Bangalore:\n {}\n".format(cities.get("Bangalore")))

#printing value of a non-existing key
print("Print the values of a non-existing key:\n {}\n".format(cities.get("Tokyo")))

#printing value of a non-existing key, returning user-defined value
print("Print the values of a non-existing key,returning user-defined value:\n {}\n".format(cities.get("Tokyo", "Key not present")))






