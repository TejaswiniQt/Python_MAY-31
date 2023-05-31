
# reversed()

name = "John"
reverse = reversed(name)
print(list(reverse))

list1 = ["Apple","Banana","Orange"]
reversed_list1 = reversed(list1)
print(list(reversed_list1))

tup1 = (10,20,30)
reversed_tup1 = reversed(tup1)
print(list(reversed_tup1))

# enumerate()

name1 = "Ram"
enumerate_name1 = enumerate(name1)
print(list(enumerate_name1))

list2 = ["Apple","Banana","Orange"]
enumerate_list2 = enumerate(list2)
print(list(enumerate_list2))

name2 = "welcome"
enumerate_name2 = enumerate(name2,5)
print(list(enumerate_name2))