sum=0
for num in range (1,100):
    sum+=num

print(sum)
print(range(1,100))

names = ("John","Mary","Hellen","Mike","McKenzie")
for name in names:
    print(name)
people = ["John","Mary","Hellen","Mike","McKenzie"]
for name in people:
    print(name)

results = [{"name":"Mary","score":468},
           {"name":"John","score":388},
           {"name":"Mike","score":291},
           {"name":"Thomas","score":322},
           {"name":"Hellen","score":378}]

print("-------------------")

for result in results:
    print(result["name"],result["score"])

