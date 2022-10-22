# Write a program to sort an array in descending order

from array import *

size = int(input("Enter the array size: "))
arr = array("i", [])
for i in range(size):
    x = int(input("Enter the array elements: "))
    arr.append(x)
temp = 0
for i in range(size):
    for j in range(i+1, size):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
print("Array in Descending order: ")
print(arr)