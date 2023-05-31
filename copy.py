# copy()

'''
list1 = [10,20,30,40]
list2 = list1.copy()
list1[2] = 50
print(list1)
print(list2)
'''

list1 = [10,20,30,40,50]
list2 = ['A','B',list1]
list3 = list2.copy()
list1[1] = 90 
print(list3)
