#a list we use []
uni = ["UON", "JKUAT", "MKU", "KU"]
cost = [50000,70000,30000,40000]

# accessing list items

print("I WILL VISIT", uni[0], "NEXT WEEK")
print("I WILL PAY", cost[2], "KES")
print(cost[1], "Is too expensive")

print("I WILL CHOOSE FROM", uni[0:3])
print("I LOVE THE FOLLOWING", uni[2:3])

uni.append("KEMU")
print(uni)
uni.remove("JKUAT")
print(uni)