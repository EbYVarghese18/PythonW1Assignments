# Program should accept an array from the user, swap the values of two arrays and display it on the console

from array import *

array1 = array('i', [])
limit = int(input("Enter the size of the array: "))
for i in range(limit):
    x = int(input("Enter the elements for array1: "))
    array1.append(x)
array2 = array('i', [])
for i in range(limit):
    x = int(input("Enter the elements for array2: "))
    array2.append(x)
print("array 1: ")
print(array1, end="")
print()
print("array 2: ")
print(array2, end="")
print()
print("Arrays after swapping: ")
temp = array1
array1 = array2
array2 = temp
print("array 1: ")
print(array1, end="")
print()
print("array 2: ")
print(array2, end="")