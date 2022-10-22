# Write a program to add to two-dimensional arrays

size = int(input("Enter the size of the array: "))
array1 = []
array2 = []
print("Enter the elements for Array 1: ")
for i in range(size):
    arrayC = []
    for j in range(size):
        arrayC.append(int(input()))
    array1.append(arrayC)
print("Enter the elements for Array 2: ")
for i in range(size):
    arrayC = []
    for j in range(size):
        arrayC.append(int(input()))
    array2.append(arrayC)
print("The sum of given array is : ")
for i in range(size):
    for j in range(size):
        print(array1[i][j] + array2[i][j], end=" ")
    print()