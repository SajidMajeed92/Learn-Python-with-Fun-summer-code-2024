# Data type List []
fruits_list = ['apple','banana','mango']
print(fruits_list)
print(type(fruits_list))
# append use to add elements in a list but at the end
fruits_list.append('water melon')
print(fruits_list)
# len count element in a list 
print(len(fruits_list))
# index will help you to find the position of an element
print(fruits_list)
print(fruits_list[:])
print(fruits_list[0:2])
print(fruits_list[0:4:2])
numbers = [1,2,3,4,5,6,10,11,12,13,14,15,16,20]
print(numbers)
print(numbers[:])
# [inclusive : exclusive]
# insert use to add element at your desired position
numbers.insert(0,0)
print(numbers)
numbers.insert(1,7)
print(numbers)
# remove delete particular element from a list
print(numbers.remove(7))
print(numbers)