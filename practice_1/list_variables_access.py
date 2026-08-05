# list
varib = ['laptop', "mouse", "keyboard","cursor","charging"]

# accessing elements in list
print(f"first item: {varib[0]}")
print(f"second item: {varib[1]}")
print(f"last item: {varib[-1]}")
print(f"first 3 items :{varib[::-2]}")

varib.append("laptop bag")
print("list of all",varib)

# append new variable
varib.append("back cover")
print("appended",varib)
# remove last variable
varib.pop()
print("pop",varib)
# remove particular variable
varib.remove("charging")
print("remove charging", varib)
# inserting new variable at index 2
varib.insert(2,"keyboard cover")
print("insert", varib)
# sorted variable
varib.sort()
print("sorted", varib)
# reverse
varib.reverse()
print("reverse", varib)
