# Write a program to find the number of even numbers in an array

from array import *

arr = array("i", [])
limit = int(input("Enter the array size: "))
for i in range(limit):
    x = int(input("Enter the array elements: "))
    arr.append(x)
evenNumberCount = 0
for i in range(limit):
    if arr[i] == 0:
        continue
    if arr[i] % 2 == 0:
        evenNumberCount = evenNumberCount + 1
print("Number of even numbers in the given array is: " + str(evenNumberCount))
