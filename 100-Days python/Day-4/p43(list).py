list = ["Dhaka", "Barishal", "Khulna", "Chittagong", "Rajshahi"]
print(list[-2])

list.append("Kushtiya")
list.extend(["Sylet", "Rangpur", "Jashor"])
print(list[-2])

list.insert(4, "Banana")
list.remove(list[-4])
list.pop(1)
#list.clear()
print(list)
