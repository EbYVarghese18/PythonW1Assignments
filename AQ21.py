# Write a program to multiply the adjacent values of
# an array and store it in an another array

size = int(input("Enter the size of array: "))
array = []
result = []
print("Enter the values of array: ")
for i in range(size):
    array.append(int(input()))
for i in range(size-1):
    result.append(array[i] * array[i+1])
print("Result: ")
for i in result:
    print(i, end=" ")