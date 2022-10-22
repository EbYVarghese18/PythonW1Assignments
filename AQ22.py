# Write a program to add the values of two 2D arrays
# Call function getArray()
# Call function addArray()
# Call function displayArray()

size = int(input("Enter the size of the array: "))


def getArray():
    print("Enter the array Elements: ")
    array = []
    for i in range(size):
        arrayTemp = []
        for j in range(size):
            arrayTemp.append(int(input()))
        array.append(arrayTemp)
    return array


def addArray(array1, array2):

    sumArray = []
    for i in range(size):
        TempArray = []
        for j in range(size):
            TempArray.append(array1[i][j] + array2[i][j])
        sumArray.append(TempArray)
        print()
    return sumArray


def displayArray(result):
    print("The sum of the given arrays is : ")
    for i in range(size):
        print(result[i])


class AddArrays:

    array1 = getArray()
    array2 = getArray()
    result = addArray(array1, array2)
    displayArray(result)