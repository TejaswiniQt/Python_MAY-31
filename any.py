# any()

list1 = [True,True]
print(any(list1))

list2 = [True,False,True]
print(any(list2))

list3 = [False]
print(any(list3))

list4 = []
print(any(list4))

dic1 = {1:"Apple",2:"Banana"}
print(any(dic1))

dic2 = {1:"Apple",0:"Banana"}
print(any(dic2))

dic3 = {False:"Apple",0:"Banana"}
print(any(dic3))

dic4 = {-1:"Apple",0:"Banana"}
print(any(dic4))