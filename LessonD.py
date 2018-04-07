names = ("John","Mary","Hellen","Mike","McKenzie")
#Tuple
# print(names)
# print(names[0])
# print(names[6])
# names[0]=("Jonny")
# print(names)

#list
cities = ["Nairobi","Mombasa","Kisumu","Kampala","Arusha","Lagos"]
print(cities[0])
print(cities[2])
cities [0] = "Abuja" #changing first city
print(cities)
cities.append("Lusaka")
print(cities)

scores = [88,45,67,43,56,78,43,78,13,56,45]
print(scores)
print(scores[4])

#dictionary
city = {"name":"Nrb","population":4000000,"continent":"Africa"}

print(city["population"])
results = [{"name":"Mary","score":468},
           {"name":"John","score":388},
           {"name":"Mike","score":291},
           {"name":"Thomas","score":322},
           {"name":"Hellen","score":378}]


student = results[2]
print(student)
print(student["name"], student["score"])

print(results)
