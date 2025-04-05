# List In python
# string - inmmutable list - mutable

marks = [94.5, 87.5,95.55,66.4,455.1]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[1])

#List slicing 
marksList = [85,66,78,89,45]
print(marks[0:3])
print(marks[2:5])
print(marks[2:])
print(marks[:3])

#Nagative indexsing
print(marks[-4:-1])

# APPEND ADDS ONE element at the end 
list = [1,2,3,4,5,6,7,8]
print(list.append(34))
print("append :",list)

# sort assending order
list = [3,45,2,67]
list.sort()
print("assending order :",list)

# dissending order
list = [45,34,12,34,1]
list.sort(reverse=True)
print("reaverse",list)

# for character
list= ["a","d","r","g","e"]
list.sort()
print(list)
list.sort(reverse=True)

# Insrt method
# list = [1,2,3,4,5,6,6,7]
# list.insert(4,6)
# print(list)

list.remove("d")

numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
numbers.


