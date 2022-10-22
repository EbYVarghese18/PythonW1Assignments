# Write a program to accept an array and display it on the console using functions

from array import *


def getArray():
    arr = array("i", [])
    size = int(input("Enter the array size: "))
    for i in range(size):
        x = int(input("Enter the element: "))
        arr.append(x)
    return arr


def displayArray(arr):
    print(arr)


array = getArray()
displayArray(array)
