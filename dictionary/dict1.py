#! /usr/bin/env/ python3

cities={"Ahmedabad":"380001", "Aizawal":"796001", "Amritsar":"143001","Bangalore":"560001","Bhopal":"462001","Bhubaneswar":"751001", "Kolkata":"700001","Imphal":"795001"}

#printing the dictionary
print(cities)

#printing all the keys of the dictionary
print("All the keys of the dictionary:\n {}\n".format(cities.keys()))

#printing all the values of the dictionary
print("All the values of the dictionary:\n {}\n".format(cities.values()))

#printing value of key Bangalore
print("Print the values of the key Bangalore:\n {}\n".format(cities["Bangalore"]))

#printing value of a non-existing key
print("Print the values of a non-existing key:\n {}\n".format(cities["Tokyo"]))





